[**Live site**](https://ceedz-73062e125056.herokuapp.com/)

# **Ceedz**

## Table of Contents

1. [Project Overview](#project-overview)
2. [User Stories](#user-stories)
   - [Guest Users](#guest-users)
   - [Registered Users](#registered-users)
   - [Administrators](#administrators)
3. [Features](#features)
   - [Existing Features](#existing-features)
   - [Features to Implement in the Future](#features-to-implement-in-the-future)
4. [Color Scheme](#color-scheme)
5. [Technologies Used](#technologies-used)
6. [Deployment](#deployment)
   - [Setting Up the Project Locally](#setting-up-the-project-locally)
   - [Deploying to GitHub](#deploying-to-github)
   - [Deploying to Heroku](#deploying-to-heroku)
7. [Credits](#credits)

## Project Overview

Welcome to the Ceedz Blog, a vibrant and interactive platform dedicated to the world of gaming. Built using the powerful Django framework, this blog serves as a hub where gamers from all walks of life can come together to share their passion for video games. Whether you're a casual player or a hardcore enthusiast, the Ceedz Blog offers a space to engage with content through likes, and explore the latest trends and news in the gaming universe.

Our platform is designed to foster a thriving community of gamers who are eager to stay up-to-date with the newest game releases, reviews, and in-depth discussions about their favorite titles. The Ceedz Blog isn't just about consuming content; it's about creating a dynamic environment where users can connect, share their unique gaming experiences, and contribute to the conversation on various gaming topics.

At the heart of the Ceedz Blog is the desire to build a connected community where the love for gaming can be shared openly and enthusiastically. Users can interact with the content by liking posts, helping to highlight popular discussions and trending topics within the community. Whether you're looking to read the latest reviews, find tips and tricks, or just want to engage with like-minded gamers, the Ceedz Blog is your go-to destination. Join us today and become a part of this exciting journey in the gaming world!

The main objective of this project is to provide a space for gamers to connect, share their experiences, and express their thoughts on various gaming topics. This project is equipped with modern functionalities such as user authentication, dynamic content updates with Cloudinary for media handling, and robust deployment practices using Heroku.

## User Stories

1. **Guest Users**:
   - As a guest user, I want to browse the blog posts without needing to register.
   - As a guest user, I want to view details of each post, including content and images.
   - As a guest user, I want to see the like count on each post but not interact with it.

2. **Registered Users**:
   - As a registered user, I want to create an account to post my own content.
   - As a registered user, I want to log in and log out of my account securely.
   - As a registered user, I want to be able to like or unlike posts to express my opinion.
   - As a registered user, I want to edit or delete my posts.
   - As a registered user, I want to see feedback messages when I perform actions such as liking or editing a post.

3. **Administrators**:
   - As an administrator, I want to manage user posts and moderate content to ensure community guidelines are followed.
   - As an administrator, I want to have access to the Django admin panel to manage all aspects of the site efficiently.
   - As an administrator (superuser), I am the only one who can see the "Admin" button in the navigation menu.

## Features

### Existing Features

1. **User Authentication**:
   - Users can register, log in, and log out.
   - Password management includes password reset and change features.

2. **Post Creation and Management**:
   - Users can create, edit, and delete their posts.
   - Each post can have a title, content, author, publication date, and an optional image.

3. **Likes System**:
   - Registered users can like or unlike posts.
   - The like button updates dynamically without needing a page refresh.

4. **Media Handling with Cloudinary**:
   - Cloudinary is used to handle media uploads, providing efficient storage and delivery of images.

5. **Responsive Design**:
   - The platform is fully responsive, ensuring a seamless experience on both desktop and mobile devices.

6. **Error Handling**:
   - Custom error pages (404, 500, 405, 403) provide a user-friendly experience when encountering issues.

7. **Admin Panel**:
   - Full access to manage posts, users, and other aspects of the platform through Django’s built-in admin interface.
   - Only the superuser can see and access the "Admin" button in the navigation bar.

8. **Header Functionality**:
   - The header includes the navigation menu and a logo that serves as the home button, streamlining navigation.
   - The home button was removed from the navigation menu to avoid redundancy, as the logo already provides this functionality.

### Features to Implement in the Future

- **Commenting System**: Allow users to comment on posts to increase interaction and discussion.
- **Profile Customization**: Enable users to customize their profiles with avatars and bios.
- **Search Functionality**: Add a search bar to help users find posts more easily.

## Color Scheme

The Ceedz Blog uses a dark-themed color scheme to provide a sleek, modern look and to reduce eye strain for users who might be reading for extended periods:

- **Background**: Black (#000000) for the main layout to create a strong contrast with the text.
- **Content Background**: Dark grey (#161c21) for content sections to distinguish them from the overall background.
- **Text**: White (#ffffff) for the main text, providing high readability against the dark background.
- **Buttons and Links**: White text with hover effects, maintaining consistency with the overall design.
- **Footer and Navigation Bar**: Dark grey (#161c21) with white text, ensuring the footer and navigation bar are clearly visible but not overpowering.

## Technologies Used

1. **Python**: The core programming language used for backend development.
2. **Django**: The web framework used to build the application, providing a robust foundation for development.
3. **Cloudinary**: A cloud service used for handling media uploads and storage.
4. **PostgreSQL**: A powerful, open-source relational database used for managing the application’s data.
5. **Heroku**: A cloud platform used for deploying the application.
6. **HTML5 & CSS3**: Used for structuring and styling the web pages.
7. **JavaScript**: For client-side scripting to handle dynamic interactions.
8. **Bootstrap**: A front-end framework to build responsive and mobile-first web pages.

## Deployment

The project is deployed on Heroku with the following steps:

1. **Setting Up the Project Locally**:
   - Clone the repository to your local machine.
   - Install the required Python packages using `pip install -r requirements.txt`.
   - Set up environment variables in an `env.py` file or directly in the Heroku environment settings.
   - Migrate the database using Django’s `python manage.py migrate` command.

2. **Deploying to GitHub**:
   1. Log into GitHub. 
   2. From the list of repositories on the screen.
   3. From the menu items near the top of the page.
   4. Scroll down to the **GitHub Pages** section.
   5. Under **Source** click the drop-down menu labelled **None** and select **Master Branch**.
   6. On selecting Master Branch the page is automatically refreshed, the website is now deployed. 
   7. Scroll back down to the **GitHub Pages** section to retrieve the link to the deployed website.

3. **Deploying to Heroku**:
   - Create a new Heroku app.
   - Add the Heroku Postgres add-on to the app for database management.
   - Set environment variables on Heroku for `SECRET_KEY`, `DEBUG`, `DATABASE_URL`, and Cloudinary credentials.
   - Push the code to the Heroku Git repository.
   - Run the `heroku run python manage.py migrate` command to apply database migrations.
   - Run `heroku run python manage.py createsuperuser` to create an admin user.
   - Deploy the app and ensure all settings are correctly configured for production.

## Credits

- **YouTube and CI Sweden Community**: For tutorials and guidance throughout the project.
- **Mentor - Brian**: For ongoing support, advice, and code reviews that greatly contributed to the project’s development.
- **Tutor Support**: Thanks to all the amazing tutors that helped me with this project.
