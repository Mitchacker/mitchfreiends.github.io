# Package and deploy to Netlify
from app_netlify_com__jit_plugin import deployToNetlify

files = [
    {"path": "index.html", "content": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Let us be friends</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <header>
            <img src="profile.jpg" alt="Profile Picture" class="profile-pic">
            <h1>Mitch Nichol</h1>
        </header>
        <section class="links">
            <a href="https://wa.link/jvzk2t" class="link-button">My Whatsapp</a>
            <a href="https://www.instagram.com/?next=%2Flivein.now%2Ftagged%2F" class="link-button">Instagram</a>
            <a href="https://x.com/Mitch_Nichol" class="link-button">Twitter</a>
            <a href="https://www.linkedin.com/in/nicholas-ayorinde-25baa8106/?originalSubdomain=ng" class="link-button">LinkedIn</a>
        </section>
    </div>
    <script src="script.js"></script>
</body>
</html>"""},

    {"path": "styles.css", "content": """body {
    margin: 0;
    font-family: Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #fbe9d0;
}

.container {
    text-align: center;
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.profile-pic {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    object-fit: cover;
}

h1 {
    margin: 10px 0;
    font-size: 24px;
}

.links {
    margin-top: 20px;
}

.link-button {
    display: block;
    margin: 10px 0;
    padding: 10px 20px;
    text-decoration: none;
    color: white;
    background-color: #007bff;
    border-radius: 5px;
    transition: background-color 0.3s;
}

.link-button:hover {
    background-color: #0056b3;
}"""},

    {"path": "script.js", "content": """// Currently, no JavaScript is required. 
// Add any interactive functionality if needed in future."""}
]

deployToNetlify(files)
