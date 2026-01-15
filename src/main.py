"""Main entry point for the To-Do List CLI application."""

import json
import os
from pathlib import Path
from typing import Optional


class AuthManager:
    """Manages user authentication and storage."""

    def __init__(self, users_file: str = "users.json"):
        """Initialize AuthManager.

        Args:
            users_file: Path to the users.json file.
        """
        self.users_file = users_file
        self._ensure_users_file()

    def _ensure_users_file(self) -> None:
        """Ensure the users.json file exists."""
        if not os.path.exists(self.users_file):
            with open(self.users_file, "w") as f:
                json.dump([], f)

    def _load_users(self) -> list:
        """Load all users from the file.

        Returns:
            List of user dictionaries.
        """
        with open(self.users_file, "r") as f:
            return json.load(f)

    def _save_users(self, users: list) -> None:
        """Save users to the file.

        Args:
            users: List of user dictionaries.
        """
        with open(self.users_file, "w") as f:
            json.dump(users, f, indent=2)

    def user_exists(self, username: str) -> bool:
        """Check if a user exists.

        Args:
            username: Username to check.

        Returns:
            True if user exists, False otherwise.
        """
        users = self._load_users()
        return any(user["username"] == username for user in users)

    def authenticate(self, username: str, password: str) -> bool:
        """Authenticate a user.

        Args:
            username: Username to authenticate.
            password: Password to verify.

        Returns:
            True if authentication successful, False otherwise.
        """
        users = self._load_users()
        for user in users:
            if user["username"] == username and user["password"] == password:
                return True
        return False

    def register_user(self, username: str, password: str) -> bool:
        """Register a new user.

        Args:
            username: Username for the new user.
            password: Password for the new user.

        Returns:
            True if registration successful, False if user already exists.
        """
        if self.user_exists(username):
            return False

        users = self._load_users()
        users.append({"username": username, "password": password})
        self._save_users(users)
        return True


class App:
    """Main CLI application."""

    def __init__(self):
        """Initialize the application."""
        self.auth_manager = AuthManager()
        self.current_user: Optional[str] = None

    def clear_screen(self) -> None:
        """Clear the terminal screen."""
        os.system("clear" if os.name == "posix" else "cls")

    def display_pre_login_menu(self) -> None:
        """Display the pre-login menu."""
        print("\n" + "=" * 40)
        print("  To-Do List Application".center(40))
        print("=" * 40)
        print("\n[1] Login")
        print("[2] Sign Up")
        print("[3] Exit")
        print("\n" + "=" * 40)

    def handle_login(self) -> bool:
        """Handle user login.

        Returns:
            True if login successful, False otherwise.
        """
        print("\n--- Login ---")
        username = input("Enter username: ").strip()

        if not username:
            print("Username cannot be empty.")
            return False

        password = input("Enter password: ").strip()

        if not password:
            print("Password cannot be empty.")
            return False

        if self.auth_manager.authenticate(username, password):
            self.current_user = username
            print(f"\nWelcome, {username}!")
            return True
        else:
            print("\nInvalid username or password.")
            return False

    def handle_signup(self) -> bool:
        """Handle user sign up.

        Returns:
            True if sign up successful, False otherwise.
        """
        print("\n--- Sign Up ---")
        username = input("Enter username: ").strip()

        if not username:
            print("Username cannot be empty.")
            return False

        if self.auth_manager.user_exists(username):
            print("Username already exists. Please choose a different one.")
            return False

        password = input("Enter password: ").strip()

        if not password:
            print("Password cannot be empty.")
            return False

        confirm_password = input("Confirm password: ").strip()

        if password != confirm_password:
            print("Passwords do not match.")
            return False

        if self.auth_manager.register_user(username, password):
            print(f"\nAccount created successfully! You can now log in.")
            return False  # Return to menu after successful signup
        else:
            print("Sign up failed. Please try again.")
            return False

    def run_pre_login_loop(self) -> bool:
        """Run the pre-login menu loop.

        Returns:
            True if user logged in, False if user chose to exit.
        """
        while True:
            self.display_pre_login_menu()
            choice = input("Choose an option: ").strip()

            if choice == "1":
                if self.handle_login():
                    return True
            elif choice == "2":
                self.handle_signup()
            elif choice == "3":
                print("\nThank you for using To-Do List Application. Goodbye!")
                return False
            else:
                print("\nInvalid choice. Please select 1, 2, or 3.")

    def run_main_loop(self) -> None:
        """Run the main application loop after login."""
        print(f"\nMain application loop for {self.current_user}")
        print("(Main to-do management features coming soon...)")

    def run(self) -> None:
        """Start the application."""
        if self.run_pre_login_loop():
            self.run_main_loop()


def main() -> None:
    """Entry point for the application."""
    app = App()
    app.run()


if __name__ == "__main__":
    main()
