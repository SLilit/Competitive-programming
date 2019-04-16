class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        sent = {}
        domains = set()
        counter = 0
        for i in range(len(emails)):
            d_index = emails[i].find('@')
            d_name = emails[i][d_index +1:]
            if d_name not in domains:
                domains.add(d_name)
                sent[d_name] = set()
                
            plus_index = emails[i][:d_index].find('+')
            if plus_index != -1:
                email = emails[i][:plus_index].replace('.','')
            else:
                email = emails[i][:d_index].replace('.','')
                
            if email not in sent[d_name]:
                sent[d_name].add(email)
                counter += 1
                
        return counter



        sent = set()
        
        for email in emails:
            local, domain = email.split("@")
            if '+' in local:
                sent.add(local[:local.index('+')].replace(".", "") + "@" + domain)
            else:
                sent.add(local.replace(".", "") + "@" + domain)
                
        return len(sent)


        seen = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.','')
            seen.add(local+'@'+domain)
        return len(seen)
                
                
                
        