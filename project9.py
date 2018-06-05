"""
CIS 15 Project 9
Simple Blog
Caitlin Baker
"""
import json 

def save_blogs(data, filename) :
    with open(filename, 'w') as f : 
        f.write(json.dumps(data, sort_keys=True, indent=2))

def load_blogs(filename) : 
    with open(filename) as f : 
        return json.loads(f.read())

def create_user(data, username, realname, email) : 
    ''' Create a user in a blog data structure 
    
    Args: 
        data - The data structure to use 
        username - The user's username 
        realname - The uers's real name 
        email - The users's email address. 
    '''
    data[username] = {}
    data[username]['name'] = realname 
    data[username]['email'] = email 
    data[username]['posts'] = []

def add_post(data, username, title, text) : 
    ''' Append the post to the user's list of blog posts. 
    
    Args:
        data - The blog data structure to use. 
        username - The user who wrote the post. 
        title - The title of the new post. 
        text - The text of the post. 
    '''
    data[username]['posts'].append({'title' : title, 'text' : text})    
    
def print_blogs(data, username) : 
    ''' Print all of the blog entries for a user.
    
    Args:
        data - The blog data structure to use. 
        username - The user to print. 
    '''
    for blog in data[username]['posts'] : 
        print ('Title:', blog['title'])
        print ('Text:', blog['text'])
        
def list_users(data):
    ''' Lists every username in the data structure
    
    Args: data - the blog data structure to use
    
    Returns a list of usernames
    '''
    usernames = []
    for username in data:
        usernames.append(username)
    
    return usernames
    
def user_summary(data, username):
    ''' Returns a list of post post title for the specified username
    
    Args: data- the blog data sturcture to use 
        username - the nmae of the user to give summary for
        
    Returns a list of titles
        
    '''
    post_titles = []
    try:
        for titles in data[username]['posts']:
            post_titles.append(titles['title'])
    except KeyError:
        print("Sorry, user does not exist.")
        return
    
    return post_titles
    
def update_user_info(data, username, new_name, new_email):
    ''' Function to update name or email for a specific username
    
    Args: data - the blog data structure to use
    username - username of the user to update_user_info
    new_name - the new name to update with
    new_email - the new email to update with
    
    Returns nothing
    '''
    try:
        if new_name != None and new_email != None:
            data[username]['name'] = new_name
            data[username]['email'] = new_email
        elif new_email != None and new_name == None:
            data[username]['email'] = new_email
        elif new_email == None and new_name != None:
            data[username]['name'] = new_name
        else:
            return
    except KeyError:
        print("Sorry, user does not exist.")
        return
        
def delete_post(data, username, post_number):
    '''
    Deletes the given post number for a specified user
    
    Args: data - the blog data structure to use
    username - name of the user to delete post from
    post_number - the index number of the desired post to delete
    
    Returns the deleted post
    '''
    try:
        try:
            deleted = data[username]['posts'].pop(post_number)
        except IndexError:
            print("Sorry, post does not exist.")
            return
    except KeyError:
        print("Sorry user does not exist.")
        return
    
    return deleted
    
def main() :
    bloggers = load_blogs('blog_data.json')
    #create_user(bloggers, 'fil', 'Fillip Foo', 'fil@foo.com')
    #add_post(bloggers, 'fil', 'Welcome to my Blog', 'This is my first post')

    #print_blogs(bloggers, 'ada')
    #print_blogs(bloggers, 'fil')
    test = list_users(bloggers)
    print(test)
    test2 = user_summary(bloggers, 'mike')
    print(test2)
    update_user_info(bloggers, 'mike', 'Mike M', 'mike@youmail.com')
    deleted = delete_post(bloggers, 'fil', 2)
    print(deleted)
    save_blogs(bloggers, 'blog_data.json.out')

if __name__ == '__main__' : 
    main()
    
