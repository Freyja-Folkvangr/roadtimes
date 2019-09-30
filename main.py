import dijkstra


def list_items_to_int(list):
    return [int('%.0f' % float(item)) for item in list]


def create_graph(matrix):
    i = 0
    j = 0
    graph = []
    while i < len(matrix):
        while j < len(matrix[i]):
            # only add the node if there is a route
            if matrix[i][j] > 0:
                graph.append((str(i), str(j), matrix[i][j]))
            j += 1
        i += 1
        j = 0
    # this prints the nodes created for dijkstra
    # print(graph)
    return dijkstra.Graph(graph)


class Trip:
    def __init__(self, graph, total_time, s, d):
        self.graph = graph
        self.total_time = total_time
        self.s = str(s)
        self.d = str(d)

    @property
    def path(self):
        return self.graph.dijkstra(self.s, self.d)[0]

    @property
    def total_distance(self):
        return self.graph.dijkstra(self.s, self.d)[1]

    # If we go from 0 to 2, but there is no route, we're forced to go to another city.
    # This property returns the full detailed path
    @property
    def sub_trips(self):
        return [[self.path[i], self.path[i + 1]] for i in range(0, len(self.path) - 1)]

    # Returns the best estimated time for a trip
    @property
    def best_time(self):
        times = []
        for item in self.sub_trips:
            times.append(self.get_edge_best_time(item[0], item[1]))
        return sum(times)

    # Prints the worst estimated time for a trip
    @property
    def worst_time(self):
        return None

    # Prints the best estimated time for a subtrip
    # Important! if you solve the equation 60 * edge.cost / 60, you'd say that best time is equals to
    # edge.cost, but after modeling a linear program and apply simplex to it, the best speed won't be 60
    def get_edge_best_time(self, start, end):
        if start == end:
            return 0
        edge = self.graph.get_edge(start, end)
        if edge:
            return 60 * edge.cost / 60
        else:
            # If there is no route in previous trips
            new = self.graph.dijkstra(start, end)
            return 60 * new[1] / 60

    # Prints the worst estimated time for a subtrip
    def get_edge_worst_time(self, start, end):
        if start == end:
            return 0
        edge = self.graph.get_edge(start, end)
        if edge:
            return 60 * edge.cost / 30
        else:
            # If there is no route in previous trips
            new = self.graph.dijkstra(start, end)
            return 60 * new[1] / 30

    # Prints the avg speed of a subtrip from a to b
    def get_edge_speed(self, start, end):
        edge = self.graph.get_edge(start, end)
        return 60 * edge.cost / (self.total_time * (1 - edge.cost / self.total_distance))


# Program START
for file in range(1, 4):
    try:
        with open('./data/{}.in'.format(file), 'r') as f:
            routes = []
            past_deliveries = []
            scheduled_queries = []
            stage = 0

            for line in f.readlines():
                line = line.replace('\n', '').split(' ')

                if stage == 0 and len(line) == 1:
                    pass
                elif stage == 1 and len(line) > 1:
                    routes.append(list_items_to_int(line))

                elif stage == 2 and len(line) > 1:
                    past_deliveries.append(list_items_to_int(line))

                elif stage == 3 and len(line) > 1:
                    scheduled_queries.append(line)

                if len(line) == 1:
                    stage += 1
            f.close()

        # calculate minimum time and speed
        the_graph = create_graph(routes)
        trips = []
        for item in past_deliveries:
            trips.append(Trip(the_graph, item[2], item[0], item[1]))

        # print results
        print('RESULTS FOR FILE {}'.format(file))
        for item in scheduled_queries:
            s = item[0]
            d = item[1]
            print(s, d, trips[0].get_edge_best_time(s, d), trips[0].get_edge_worst_time(s, d))

            #Search the history of trips
            #print(s, d, trips[0].get_edge_best_time(s, d), trips[0].get_edge_worst_time(s, d))
        # print(routes)
        # print(past_deliveries)
        # print(the_graph.dijkstra('0', '2'))

    except() as err:
        print(err)
