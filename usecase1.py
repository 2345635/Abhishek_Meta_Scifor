{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOa441hITxq7z1iMXr8up9H",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/2345635/Abhishek_Scifor/blob/main/usecase1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class Bank:\n",
        "    def __init__(self, pin, balance):\n",
        "        self._pin = pin\n",
        "        self._balance = balance\n",
        "    def _verify_pin(self, pin):\n",
        "        return self._pin == pin\n",
        "    def get_balance(self):\n",
        "        return self._balance\n",
        "    def _update_balance(self, amount):\n",
        "        self._balance += amount\n",
        "        print(f\"Updated balance: {self._balance}\")\n",
        "    def withdraw(self, pin, amount):\n",
        "        if self._verify_pin(pin):\n",
        "            if self._balance >= amount:\n",
        "                self._update_balance(-amount)\n",
        "                print(f\"Withdrawal successful. Withdrawn amount: {amount}\")\n",
        "            else:\n",
        "                print(\"Insufficient balance\")\n",
        "        else:\n",
        "            print(\"Invalid pin\")\n",
        "    def deposit(self, pin, amount):\n",
        "        if self._verify_pin(pin):\n",
        "            self._update_balance(amount)\n",
        "            print(f\"Deposit successful. Deposited amount: {amount}\")\n",
        "        else:\n",
        "            print(\"Invalid pin\")"
      ],
      "metadata": {
        "id": "4iEqBMt9R1Hc"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "pin = int(input(\"Enter your PIN: \"))\n",
        "initial_balance = float(input(\"Enter your initial balance: \"))\n",
        "bank_account = Bank(pin, initial_balance)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZJSzs39MS6Cg",
        "outputId": "501a4bce-a56f-4eb4-af2a-743d0a87d07a"
      },
      "execution_count": 4,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Enter your PIN: 123\n",
            "Enter your initial balance: 4000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "while True:\n",
        "    action = input(\"Enter 'withdraw' to withdraw money or 'deposit' to deposit money (or 'exit' to exit): \").lower()\n",
        "    if action == 'withdraw':\n",
        "        pin_input = int(input(\"Enter your PIN: \"))\n",
        "        amount = float(input(\"Enter the amount to withdraw: \"))\n",
        "        bank_account.withdraw(pin_input, amount)\n",
        "    elif action == 'deposit':\n",
        "        pin_input = int(input(\"Enter your PIN: \"))\n",
        "        amount = float(input(\"Enter the amount to deposit: \"))\n",
        "        bank_account.deposit(pin_input, amount)\n",
        "    elif action == 'exit':\n",
        "        break\n",
        "    else:\n",
        "        print(\"Invalid action\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "X_OEx-rcTCeI",
        "outputId": "3a7f7c6e-aa20-46c0-8a65-8db5b5282e82"
      },
      "execution_count": 5,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Enter 'withdraw' to withdraw money or 'deposit' to deposit money (or 'exit' to exit): withdraw\n",
            "Enter your PIN: 123\n",
            "Enter the amount to withdraw: 1000\n",
            "Updated balance: 3000.0\n",
            "Withdrawal successful. Withdrawn amount: 1000.0\n",
            "Enter 'withdraw' to withdraw money or 'deposit' to deposit money (or 'exit' to exit): deposit\n",
            "Enter your PIN: 123\n",
            "Enter the amount to deposit: 250\n",
            "Updated balance: 3250.0\n",
            "Deposit successful. Deposited amount: 250.0\n",
            "Enter 'withdraw' to withdraw money or 'deposit' to deposit money (or 'exit' to exit): exit\n"
          ]
        }
      ]
    }
  ]
}