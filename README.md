<<<<<<< HEAD
# 🎮 Web Tetris Game

A modern, web-based Tetris game built with Flask and JavaScript. Play the classic puzzle game in your browser with beautiful graphics and smooth gameplay!

## ✨ Features

- **Modern Web Interface** - Beautiful, responsive design with gradient backgrounds
- **User Management** - Save scores and track progress for multiple players
- **Multiple Difficulty Levels** - Easy, Medium, and Hard modes
- **Full Tetris Experience** - All 7 classic Tetris pieces (I, O, T, L, J, S, Z)
- **Rotation System** - Rotate blocks with wall kick mechanics
- **Score Tracking** - Persistent score history for returning players
- **Mobile Friendly** - Responsive design that works on all devices

## 🎯 How to Play

### Controls
- **← →** - Move block left/right
- **↑** - Rotate block (90° clockwise)
- **↓** - Soft drop (move down faster)
- **Space** - Hard drop (instant drop)
- **P** - Pause/Resume game

### Game Rules
- Clear horizontal lines to score points
- Lines disappear when completely filled
- Game ends when blocks reach the top
- Score more points by clearing multiple lines at once

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/web-tetris.git
   cd web-tetris
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the game**
   ```bash
   python web_tetris.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:3000`

## 📁 Project Structure

```
web-tetris/
├── web_tetris.py          # Main Flask application
├── templates/
│   └── index.html         # Game interface
├── users.json             # User data and scores (created automatically)
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🛠️ Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Modern CSS with gradients and animations
- **Data Storage**: JSON file-based storage

## 🎨 Features in Detail

### User Management
- Enter username to start playing
- Automatic score tracking
- View previous scores for returning players
- Session-based gameplay

### Difficulty Levels
- **Easy**: Slower falling speed, great for beginners
- **Medium**: Standard speed, balanced gameplay
- **Hard**: Fast-paced, challenging experience

### Scoring System
- 100 points per line cleared
- Bonus points for multiple lines
- Level progression based on lines cleared
- Hard drop bonus points

## 🔧 Customization

You can easily customize the game by modifying:

- **Game speed**: Edit `difficulty_speeds` in `web_tetris.py`
- **Board size**: Change `board_width` and `board_height`
- **Colors**: Modify CSS variables in `templates/index.html`
- **Scoring**: Adjust point values in the JavaScript code

## 🐛 Troubleshooting

### Port Already in Use
If you get "Address already in use" error:
- Change the port in `web_tetris.py` (line with `app.run()`)
- Or stop other services using port 3000

### Installation Issues
- Make sure you have Python 3.7+ installed
- Try using `pip3` instead of `pip`
- Install dependencies with `--user` flag if needed

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Inspired by the classic Tetris game
- Built with modern web technologies
- Designed for fun and learning

---

**Enjoy playing Tetris! 🎮**

*Built with ❤️ using Flask and JavaScript*
=======
# web-tetris
>>>>>>> 5c4fe660c6c36ad9416ce5a4155fa06b5b2d4e7a
