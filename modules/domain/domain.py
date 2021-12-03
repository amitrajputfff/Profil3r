import requests
import time

class Domain:

    def __init__(self, config, permutations_list):
        # 100 ms
        self.delay = config['plateform']['domain']['rate_limit'] / 1000
        # {permutation}.{tld}
        self.format = config['plateform']['domain']['format']
        # Top level domains
        self.tld = config['plateform']['domain']['TLD']
        # domains are not case sensitive
        self.permutations_list = [perm.lower() for perm in permutations_list]
        # domain
        self.type = config['plateform']['domain']['type']

    # Generate all potential domains names
    def possible_domains(self):
        possible_domains = []

        # search all TLD (.com, .net, .org...), you can add more in the config.json file
        for domain in self.tld:
            for permutation in self.permutations_list:
                possible_domains.append(self.format.format(
                    permutation = permutation,
                    domain = domain
                ))

        return possible_domains

    def search(self):
        domains_lists = {
            "type": self.type,
            "accounts": []
        }
        possible_domains_list = self.possible_domains()

        r = None
        for domain in possible_domains_list:
            try:
                r = requests.head(domain, timeout=5)
            except requests.ConnectionError:
                pass

            # If the domain exists
            if r is not None and r.status_code < 400:
                domains_lists["accounts"].append({"value": domain})
            time.sleep(self.delay)
        
        return domains_lists 
