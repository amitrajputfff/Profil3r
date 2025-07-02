import questionary

# The menu displays a list of checkboxes, which allows the user to select the separators and modules he wants to use
def menu(self):
    #
    # SEPARATORS
    #

    # Get a list of all existing separators
    separators = self.CONFIG["separators"]

    separator_choices = []
    for separator, value in separators.items():
        # Add separator as a choice with description
        separator_choices.append(questionary.Choice(
            title=f"{value} ({separator} - Example: john{value}doe)",
            value=value
        ))

    self.separators = questionary.checkbox(
        message='⚙️  Select separators',
        choices=separator_choices
    ).ask()

    #
    # SERVICES
    #

    # Get a list of all existing modules
    modules_list = sorted([module for module in self.CONFIG["plateform"]])
    # Create a list of all existing categories
    categories = sorted(list(set([content["type"] for module, content in self.CONFIG["plateform"].items()])))
    
    service_choices = []
    
    for category in categories:
        # Add category separator
        service_choices.append(questionary.Separator(category.upper()))
        # Append category items
        for module in modules_list: 
            if self.CONFIG["plateform"][module]["type"] == category:
                service_choices.append(questionary.Choice(
                    title=module,
                    value=module,
                    checked=module in self.CONFIG["report_elements"]
                ))
    
    def validate_services(answer):
        if len(answer) == 0:
            return 'You must choose at least one service !'
        return True
    
    modules = questionary.checkbox(
        message='⚙️  Select services',
        choices=service_choices,
        validate=validate_services
    ).ask()
    
    self.modules_update(modules)
