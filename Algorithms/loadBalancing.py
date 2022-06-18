def loadBalancing(k, arrivals, durations) -> list:
    """ Finds the most used server given request arrival times and duration of requests for a given number of
    servers assuming round robin load balancing
    :param k: number of servers (IDs: 1...k)
    :param arrivals: arrival times of each request
    :param durations: duration of each request
    :return list of the most used server ID (multiple server IDs if same amount of usage)
    """
    
    # queue of server IDs for round robin scheduling
    servers = list(range(1, k+1))
    
    # keep track of current request duration and also the total duration on each server
    server_info = {server: {"total_usage": 0, "curr_duration_left": 0 } for server in servers}
    
    
    curr_time = 0
    while arrivals: #keep going while still new requests to serve

        # obtain the next request (earliest arrival first)
        next_request_index = arrivals.index(min(arrivals))
        next_request_arrival = arrivals[next_request_index]
        next_request_duration = durations[next_request_index]

        # Either no new requests or no servers available
        if next_request_arrival > curr_time or len(servers) == 0:
            curr_time += 1
            servers, server_info = update_servers(servers, server_info)
            continue

        # Start using an available server and store the request info
        free_server = servers.pop(0)
        server_info[free_server]['total_usage'] += next_request_duration
        server_info[free_server]["curr_duration_left"] = next_request_duration + 1
        
        # Get ready to serve next request - remove the current request arrival and duration
        del arrivals[next_request_index]
        del durations[next_request_index]

        # free up servers if they are done processing their current request
        servers, server_info = update_servers(servers, server_info)
        curr_time += 1
    
    

    # Find the maximum usage out of all the servers
    max_usage = max(server_info.items(), key=lambda x: x[1]['total_usage'])[1]['total_usage']

    # Find the server(s) ID that had the maximum usage
    most_used_id = []
    for server in server_info:
        if server_info[server]['total_usage'] == max_usage:
            most_used_id.append(server)
    # Return in ascending order
    most_used_id.sort()
    return most_used_id

def update_servers(servers, server_info):
    """ Iterate through the servers and update the usage info for those in current use, add free'd up servers to back of queue (round robin)
    :param servers: current queue of available servers
    :param server_info: info on all servers
    :return updated server queue and server_info
    """

    for server in server_info:
        if server not in servers:

            if server_info[server]["curr_duration_left"] == 0: # Done serving request, free up server
                servers.append(server)
            else:
                server_info[server]["curr_duration_left"] -= 1
    return servers, server_info
        




# Driver program to test above functions
if __name__=='__main__':
	
    # Test case
    number_servers = 3
    arrival_times = [1,2,4,5,7,1,3,4,5,6,7,8,9,0,2,5,2,4,5,10,66,55,21,43,11,2,101,10000,2,5,2,4,5,10,66,55,21,43,11,2,101,2,5,2,4,5,10,66,55,21,43,11,2,101,2,5,2,4,5,10,66,55,21,43,11,2,101,]
    durations = [2,5,2,4,5,10,66,55,21,43,11,2,101,10000,2,5,2,4,5,10,66,55,21,43,11,2,101,10000,2,5,2,4,5,10,66,55,21,43,11,2,101,2,5,2,4,5,10,66,55,21,43,11,2,101,2,5,2,4,5,10,66,55,21,43,11,2,101,]

    assert len(durations) == len(arrival_times)
    
    most_used = loadBalancing(number_servers, arrival_times, durations)
    print(f"Most used servers: {most_used}")

	
