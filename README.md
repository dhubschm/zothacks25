# Frontend Starter Pack
This repository contains starter code for a basic HTML/CSS/Javascript website.

## Intro
The frontend of a website boils down to 3 components:
- how the site is structured (HTML)
- how the site looks (CSS)
- how the site functions (Javascript/JS).

In this demo, we'll be using pure HTML/CSS/Javascript. It is a compilation of HTML, CSS, JS starting ideas and concepts that you can use for your ZotHacks project or whatever project you want.

## How to get this code
1. We highly recommend installing [Git](https://git-scm.com/install/) and cloning the repository.
   
   Run this command to get all of the files in this repository:
   
   ```bash
   git clone https://github.com/HackAtUCI/zothacks-frontend-startercode.git
   ```
2. You could also download the code as a zip by clicking on the green "Code" button and clicking "Download ZIP".

   Then, you can extract into a folder and open the folder in your favorite code editor.
   <img width="940" height="459" alt="image" src="https://github.com/user-attachments/assets/1cdd0c0d-9296-4125-b327-ec26e6a6eaf6" />


## How to run your code
- You can drag the HTML file into your browser to see all of your changes!
- If you use VSCode, there are some extensions that make developing frontend apps much easier.

## Extensions

### Live Server
If you use VSCode, you can get the [Live Server Extension](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer). 

Any change you make will be directly reflected in the website instead of you having to drag the HTML file into your browser again.

1. Navigate to the Extensions tab in VSCode, search for "live server", click the top option, and click on the blue install button in the top center.
   
<img width="1919" height="997" alt="image" src="https://github.com/user-attachments/assets/ede926fe-933f-47e4-9803-691ba976b95f" />

2. Select `index.html` and click on the "Go Live" button in the bottom of VSCode. Your browser should automatically open with the HTML file rendered!
   
   <img width="561" height="221" alt="image" src="https://github.com/user-attachments/assets/d35f82f7-b4c1-43f3-ba38-e4b88d492470" />

Congratulations! Now whenever you edit your HTML, CSS, or JS file, your changes are automatically reflected in your browser.

Try changing "Hello, world!" to something different and see your changes appear in the browser!



### Live Share
If you use VSCode and need to collaborate on the same project (like in a hackthon!), you can get the [Live Share Extension](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare).

This allows multiple people to edit the same file at the same time, just like how multiple people can edit a Google Doc at the same time.

You can also use this with the [Live Server Extension](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)! 

**Note: The following steps will require 2 or more computers. One computer (Computer 1) has the code and this extension. Another computer (Computer 2) simply needs to connect to the session (will be explained in the next steps). All other computers can follow Computer 2's steps.**

1. On Computer 1, navigate to the Extensions tab in VSCode, search for "live share", click the top option, and click on the blue install button in the top center.

<img width="1919" height="998" alt="image" src="https://github.com/user-attachments/assets/57b7c061-62b5-43c6-8349-afc7194ec0d9" />

2. On Computer 1, click on the "Live Share" button in the bottom of VSCode. Click the button. You will be prompted to sign into GitHub or Microsoft.

<img width="414" height="133" alt="image" src="https://github.com/user-attachments/assets/6845e465-7a35-4ca3-8e06-bffc51a2e99f" />

3. Once you sign in, you will see a notification starting a session and later, `Invitation link copied to clipboard!`. Send this link to Computer 2.

<img width="481" height="132" alt="image" src="https://github.com/user-attachments/assets/25a7f785-6d53-42c8-965c-70149d4696c0" />

4. On Computer 2, navigate to the link. You can choose to open VSCode locally or use the web. You may be asked to sign in.

<img width="505" height="143" alt="image" src="https://github.com/user-attachments/assets/50a6f959-2f73-4805-a3df-73a4b72e5c29" />

5. On Computer 1, you will see a notification to approve someone to join the collaboration session. Click "Accept read-write" so Computer 2 can edit the files.

<img width="491" height="148" alt="image" src="https://github.com/user-attachments/assets/5777d850-058e-4005-8915-c7a418b6350a" />

6. On Computer 2, you will see that the same code from Computer 1 shows up with Computer 1's cursor active.

<img width="1919" height="795" alt="image" src="https://github.com/user-attachments/assets/459686a1-fa5b-4227-8911-2ec5da5cc3ec" />

Congratulations! You can now have multiple users edit the same files at the same time!


## Notes about HTML
There are a few things we want to point out about HTML files. You can look at the comments in `index.html` for detailed examples and explanations.

### 1. Overall structure

Everything is composed of tags. Notice how the `title` tag here has an opening and closing tag to enclose the title.
```html
<title>My App</title>
```

Everyting is composed of tags and nested tags. Nesting simply means we place a tag inside another. In this example, the `img` image tag is placed in the `a` anchor tag:
```html
<a href="https://youtu.be/GtL1huin9EE">
    <img id="petr" src="petr.png" alt="petr"/>
</a>
```

### 2. Linking CSS
   
Near the top of `index.html`, you'll see this:

```html
<link rel="stylesheet" href="styles.css" />
```

This code allows the styles from `styles.css` to affect your html code. Note that `styles.css` is its own file in the same folder as `index.html`.

### 3. Linking JS
   
Near the bottom of `index.html`, you'll see this:

```html
<script src="script.js"></script>
```

This code allows the javascript code from `script.js` to affect your html (and maybe css) code. Note that `script.js` is its own file in the same folder as `index.html`.


## Resources
Google and documentation are your best friends!
- Don't know what an HTML tag does? Look it up or go to the [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements).
- Don't know what a selector is or what certain styles do? Look it up or go to the [MDN CSS Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference).
- Don't know what some javascript function does or how to add interactivity to your HTML file? Look it up or go to the [MDN JS Docs](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Adding_interactivity).

If you've never built a website before, here are a few resources to get you started.
- [What is an API?](https://medium.com/@perrysetgo/what-exactly-is-an-api-69f36968a41f) 
- [How to Make API Requests](https://medium.com/swlh/making-use-of-apis-in-your-front-end-c168e343bea3): Get data using a frontend.
- [HTTP Requests](https://www.w3schools.com/tags/ref_httpmethods.asp): How the internet communicates. Whenever you go to a URL or submit a form, there is a request that is sent to get or change information.

If you're feeling more advanced, here are some other resourses to expand your front end knowledge,
- [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/) - CSS library that containing preset styles
- [SASS/SCSS](https://sass-lang.com/) - CSS scripting framework that can potentially give you a more intuitive view on CSS (nested CSS)
- [Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) - Allow you to structure and space out your elements in pure CSS. You can see this in action when you are using the `display: flex;` styling in your container element.
- [React](https://reactjs.org/tutorial/tutorial.html) - A JavaScript framework that allows you to build your website using the idea of components.
