from mediawiki import MediaWiki

wikipedia = MediaWiki()

def getlinks(page_title):
    page = wikipedia.page(page_title)
    return page.links

def getbacklinks(page_title):
    page = wikipedia.page(page_title)
    return page.backlinks

def bidirectional_bfs(start_page, end_page):
    if start_page == end_page:
        return [start_page]

    # Queues for BFS
    forward_queue = [(start_page, [start_page])]
    backward_queue = [(end_page, [end_page])]

    # Sets to keep track of visited nodes
    forward_visited = {start_page}
    backward_visited = {end_page}

    # Dictionaries to store the paths
    forward_paths = {start_page: [start_page]}
    backward_paths = {end_page: [end_page]}

    while forward_queue and backward_queue:
        # Forward search step
        if forward_queue:
            current_page, path = forward_queue.pop(0)
            links =  getlinks(current_page)
            for link in links:
                if link not in forward_visited:
                    forward_visited.add(link)
                    new_path = path + [link]
                    forward_paths[link] = new_path
                    forward_queue.append((link, new_path))
                    if link in backward_visited:
                        return new_path[:-1] + backward_paths[link][::-1]

        # Backward search step
        if backward_queue:
            current_page, path = backward_queue.pop(0)
            backlinks =  getbacklinks(current_page)
            for backlink in backlinks:
                if backlink not in backward_visited:
                    backward_visited.add(backlink)
                    new_path = path + [backlink]
                    backward_paths[backlink] = new_path
                    backward_queue.append((backlink, new_path))
                    if backlink in forward_visited:
                        return forward_paths[backlink][:-1] + new_path[::-1]

    return None  # No path found

# Heuristic for Homegrown DFS
def HeuristicForward(page):
    links =  getlinks(page)
    hf = len(links)
    links = getbacklinks(page)
    hf += .5*len(links)
    return hf

def HeuristicBackward(page):
    links =  getlinks(page)
    hb = .5*len(links)
    links = getbacklinks(page)
    hb += len(links)
    return hb

def bidirectional_dfs(start_page, end_page):
    if start_page == end_page:
        return [start_page]

    # Queues for BFS
    forward_queue = [(start_page, [start_page], HeuristicForward(start_page))]
    backward_queue = [(end_page, [end_page], HeuristicBackward(end_page))]

    # Sets to keep track of visited nodes
    forward_visited = {start_page}
    backward_visited = {end_page}

    # Dictionaries to store the paths
    forward_paths = {start_page: [start_page]}
    backward_paths = {end_page: [end_page]}

    while forward_queue and backward_queue:
        
        # Forward search step
        if forward_queue:

            #  of popping the first in the list, pop the one with the most number of links
            forward_queue.sort(key = lambda x: x[2], reverse = True)
            current_page, path, heuristicf = forward_queue.pop(0)
            
            
            links =  getlinks(current_page)
            for link in links:
                if link not in forward_visited:
                    forward_visited.add(link)
                    new_path = path + [link]
                    forward_paths[link] = new_path
                    forward_queue.append((link, new_path,HeuristicForward(link)))
                    if link in backward_visited:
                        return new_path[:-1] + backward_paths[link][::-1]

        # Backward search step
        if backward_queue:
            
            # Instead of popping the first in the list, pop the one with the most number of links
            backward_queue.sort(key = lambda x: x[2], reverse = True)
            current_page, path, heuristicb = backward_queue.pop(0)   
            

            backlinks =  getbacklinks(current_page)
            for backlink in backlinks:
                if backlink not in backward_visited:
                    backward_visited.add(backlink)
                    new_path = path + [backlink]
                    backward_paths[backlink] = new_path
                    backward_queue.append((backlink, new_path, HeuristicBackward(backlink)))
                    if backlink in forward_visited:
                        return forward_paths[backlink][:-1] + new_path[::-1]


    return None  # No path foundound

# Wrapper function to run the async code
def find_path(start_page, end_page, alg):
    if(alg==1):
        return (bidirectional_bfs(start_page, end_page))
    elif(alg==2):
        return (bidirectional_dfs(start_page, end_page))

# Test Run
start_page = "Graffito_(archaeology)"
end_page = "Trumbo_Point"
path = find_path(start_page, end_page, 1)

print(path)

start_page = "Itinerant poet"
end_page = "Early medieval European dress"
path = find_path(start_page, end_page, 2)

print(path)
