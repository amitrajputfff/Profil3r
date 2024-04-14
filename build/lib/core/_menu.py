from PyInquirer import prompt, Separator

# The menu displays a list of checkboxes, which allows the user to select the separators and modules he wants to use
def menu(self):
    #
    # SEPARATORS
    #

    # Get a list of all existing separators
    separators = self.CONFIG["separators"]

    separators_menu = [
        {
            'type': 'checkbox',
            'qmark': '⚙️ ',
            'message': 'Select separators',
            'name': 'separators',
            'choices': []
        }
    ]

    for separator, value in separators.items():
        # Separator title
        separators_menu[0]["choices"].append(Separator("{} - Exemple : john{}doe".format(separator, value)))
        # Separator
        separators_menu[0]["choices"].append({"name": value})

    self.separators = prompt(separators_menu)["separators"]

    #
    # SERVICES
    #

    # Get a list of all existing modules
    modules_list = sorted([module for module in self.CONFIG["plateform"]])
    # Create a list of all existing categories
    categories = sorted(list(set([content["type"] for module, content in self.CONFIG["plateform"].items()])))
    
    services_menu = [
        {
            'type': 'checkbox',
            'qmark': '⚙️ ',
            'message': 'Select services',
            'name': 'modules',
            'choices': [
                
            ],
            'validate': lambda answer: 'You must choose at least one service !' \
                if len(answer) == 0 else True
        }
    ]

    for category in categories:
        # Category title 
        services_menu[0]["choices"].append(Separator(category.upper()))
        # Append category items
        for module in modules_list: 
            if self.CONFIG["plateform"][module]["type"] == category:
                services_menu[0]["choices"].append(
                    {
                        'name': module,
                        # Checked by default
                        'checked': module in self.CONFIG["report_elements"]
                    })
    
    modules = prompt(services_menu)["modules"]
    self.modules_update(modules)