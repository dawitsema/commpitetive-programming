class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subdomain_counter = {}

        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")

            count = int(count)

            subdomains = domain.split(".")

            for i in range(len(subdomains)):
                subdomain = ".".join(subdomains[i:])
                subdomain_counter[subdomain] = subdomain_counter.get(subdomain, 0) + count

        store = []
        
        for subdomain, count in subdomain_counter.items():
            store.append(f"{count} {subdomain}")

        return store
