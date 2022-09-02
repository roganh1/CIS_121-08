from breezypythongui import EasyFrame
from tkinter import HORIZONTAL

account_bal = 5000


class Tax(EasyFrame):
    """Top-notch quality personal finance software"""

    def __init__(self):
        """Window Set-Up."""
        EasyFrame.__init__(title="Janky Accounting Software 3.0")

        # Label and text box that shows the users account balance.
        self.addLabel(text="Account Balance", row=0, column=0)
        self.addTextField(text=account_bal, row=0, column=1, columnspan=3)

        # Label and field for what the user wants to do.
        self.addLabel(text="Type of action:", row=1, column=0)
        self.action_type = self.addRadiobuttonGroup(row=1, column=1, columnspan=2, orient=HORIZONTAL)
        default_status = self.action_type.addRadiobutton(text="Deposit")
        self.action_type.setSelectedButton(default_status)
        self.action_type.addRadiobutton(text="Withdraw")
