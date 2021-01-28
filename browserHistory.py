'''
You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) 
    Initializes the object with the homepage of the browser.

void visit(string url) 
    Visits url from the current page. It clears up all the forward history.

string back(int steps) 
    Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.

string forward(int steps) 
    Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
'''


class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        if self.curr == len(self.history):
            self.history.append(url)
        else:
            self.history[self.curr] = url
        self.bound = self.curr

    def back(self, steps: int) -> str:
        self.curr = max(0, self.curr - steps)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(self.curr + steps, self.bound)
        return self.history[self.curr]


if __name__ == "__main__":
    # Your BrowserHistory object will be instantiated and called as such:
    browserHistory = BrowserHistory("leetcode.com")
    print(browserHistory.visit("google.com"))
    # You are in "leetcode.com". Visit "google.com"
    print(browserHistory.visit("facebook.com"))
    # You are in "google.com". Visit "facebook.com"
    print(browserHistory.visit("youtube.com"))
    # You are in "facebook.com". Visit "youtube.com"
    print(browserHistory.back(1))
    # You are in "youtube.com", move back to "facebook.com" return "facebook.com"
    print(browserHistory.back(1))
    # You are in "facebook.com", move back to "google.com" return "google.com"
    print(browserHistory.forward(1))
    # You are in "google.com", move forward to "facebook.com" return "facebook.com"
    print(browserHistory.visit("linkedin.com"))
    # You are in "facebook.com". Visit "linkedin.com"
    print(browserHistory.forward(2))
    # You are in "linkedin.com", you cannot move forward any steps.
    print(browserHistory.back(2))
    # You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
    print(browserHistory.back(7))
    # You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
