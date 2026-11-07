class Solution:
    def countServers(self, n, logs, x, queries):

        logs.sort(key=lambda log: log[1])

        sorted_queries = sorted(
            (q, i) for i, q in enumerate(queries)
        )

        result = [0] * len(queries)
        servers = {}

        left = right = 0
        m = len(logs)

        for q, idx in sorted_queries:

            while right < m and logs[right][1] <= q:
                server = logs[right][0]
                servers[server] = servers.get(server, 0) + 1
                right += 1

            while left < right and logs[left][1] < q - x:
                server = logs[left][0]
                servers[server] -= 1

                if servers[server] == 0:
                    del servers[server]

                left += 1

            result[idx] = n - len(servers)

        return result