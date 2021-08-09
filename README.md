# CalPolyLogin (supports **Firefox** only as of right now)
This a simple shortcut that can be run from your command line. It will launch a Firefox window that automatically logs you into your Cal Poly portal,
and it takes into account Duo authentication.

System requirements:
- [Selenium](https://pypi.org/project/selenium/)
- [Geckodriver](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwj4xvqm8qLyAhWxGqYKHQTvB80QFnoECBkQAw&url=https%3A%2F%2Fgithub.com%2Fmozilla%2Fgeckodriver%2Freleases&usg=AOvVaw0SNTcgCJ-U5zHaleZqKe5q)

## How to Use
1. Open up your system's terminal
2. Navigate to directory where the script is located at

As an example:
```
cd Documents/GitHub/CalPolyLogin
```
3. Run the following command
```
Python3 ./CalPolyLogin
```
4. For the first time running it, it will prompt you for your username and password
5. Authenticate the login by going on your phone and pressing the green check mark on the Duo app
6. You are now logged in!
