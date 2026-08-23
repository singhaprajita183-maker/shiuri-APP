import sys
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QPushButton, QLineEdit, QStackedWidget, QFrame, QGridLayout, QMessageBox
)

class ShioriApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shiori (栞) - Circular Learning Network")
        self.resize(1100, 750)
        self.setStyleSheet("""
            QMainWindow { background-color: #07090E; }
            QLabel { color: #FFFFFF; font-family: 'Segoe UI', sans-serif; }
            QPushButton { 
                background: linear-gradient(135deg, #6366F1, #8B5CF6); 
                background-color: #6366F1;
                color: white; 
                border-radius: 10px; 
                padding: 8px 16px; 
                font-weight: bold; 
            }
            QPushButton:hover { background-color: #4F46E5; }
            QLineEdit { 
                background-color: #111827; 
                border: 1px solid #1F2937; 
                color: white; 
                padding: 8px 12px; 
                border-radius: 12px; 
            }
        """)

        # Main Layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # 1. Navbar
        navbar = QFrame()
        navbar.setStyleSheet("background-color: #0B0F19; border-bottom: 1px solid #1F2937;")
        nav_layout = QHBoxLayout(navbar)
        
        brand = QLabel("栞 Shiori")
        brand.setStyleSheet("font-size: 20px; font-weight: bold; color: white;")
        
        search_bar = QLineEdit()
        search_bar.setPlaceholderText("Search books, authors, ISBN...")
        search_bar.setFixedWidth(350)
        
        scan_btn = QPushButton("📷 AI Scan")
        scan_btn.clicked.connect(lambda: self.switch_page(1))
        
        pts_badge = QLabel("🌱 1,250 pts")
        pts_badge.setStyleSheet("color: #34D399; background: rgba(16, 185, 129, 0.15); padding: 6px 12px; border-radius: 12px; font-weight: bold;")
        
        nav_layout.addWidget(brand)
        nav_layout.addWidget(search_bar)
        nav_layout.addWidget(scan_btn)
        nav_layout.addWidget(pts_badge)
        main_layout.addWidget(navbar)

        # 2. Module Nav Tabs
        tab_frame = QFrame()
        tab_frame.setStyleSheet("background-color: #0B0F19;")
        tab_layout = QHBoxLayout(tab_frame)
        
        modules = [
            ("📚 Feed", 0), ("📷 AI Vision Scanner", 1), 
            ("🔄 Smart Exchange", 2), ("🛡️ Trust & Safety", 3), ("🌱 ESG Dashboard", 4)
        ]
        
        for name, index in modules:
            btn = QPushButton(name)
            btn.setStyleSheet("background-color: #1F2937; color: white; border: none; font-size: 12px;")
            btn.clicked.connect(lambda checked, idx=index: self.switch_page(idx))
            tab_layout.addWidget(btn)
            
        main_layout.addWidget(tab_frame)

        # 3. Stacked Pages Module
        self.pages = QStackedWidget()
        
        self.pages.addWidget(self.create_feed_page())
        self.pages.addWidget(self.create_scanner_page())
        self.pages.addWidget(self.create_exchange_page())
        self.pages.addWidget(self.create_safety_page())
        self.pages.addWidget(self.create_esg_page())
        
        main_layout.addWidget(self.pages)

    def switch_page(self, index):
        self.pages.setCurrentIndex(index)

    # PAGE 1: FEED
    def create_feed_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        title = QLabel("Learn. Share. Grow. Together.")
        title.setStyleSheet("font-size: 28px; font-weight: bold; color: white; margin-top: 10px;")
        sub = QLabel("Buy, Sell, Donate or Swap educational materials in your community.")
        sub.setStyleSheet("color: #9CA3AF; font-size: 14px;")
        
        layout.addWidget(title)
        layout.addWidget(sub)
        
        # Grid Books
        grid = QGridLayout()
        books = [
            ("NCERT Physics Class 11", "₹280", "Aarav S."),
            ("Mathematics Class 12", "₹320", "Diya S."),
            ("Organic Chemistry Class 12", "₹350", "Rohan D."),
            ("Indian Polity UPSC", "₹180", "Meera I.")
        ]
        
        for idx, (b_title, price, seller) in enumerate(books):
            card = QFrame()
            card.setStyleSheet("background-color: #111827; border: 1px solid #1F2937; border-radius: 12px; padding: 10px;")
            c_layout = QVBoxLayout(card)
            
            t_lbl = QLabel(f"<b>{b_title}</b>")
            s_lbl = QLabel(f"Seller: {seller}")
            s_lbl.setStyleSheet("color: #9CA3AF;")
            p_lbl = QLabel(f"<b>{price}</b>")
            p_lbl.setStyleSheet("color: #34D399; font-size: 16px;")
            
            buy_btn = QPushButton("Buy")
            
            c_layout.addWidget(t_lbl)
            c_layout.addWidget(s_lbl)
            c_layout.addWidget(p_lbl)
            c_layout.addWidget(buy_btn)
            
            grid.addWidget(card, idx // 2, idx % 2)
            
        layout.addLayout(grid)
        layout.addStretch()
        return page

    # PAGE 2: SCANNER
    def create_scanner_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        title = QLabel("📷 AI Vision Scanner")
        title.setStyleSheet("font-size: 22px; font-weight: bold;")
        layout.addWidget(title)
        
        scan_box = QFrame()
        scan_box.setStyleSheet("background-color: #111827; border: 2px dashed #374151; border-radius: 16px;")
        sb_layout = QVBoxLayout(scan_box)
        
        self.res_lbl = QLabel("Click scan to detect book details")
        self.res_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        btn_sim = QPushButton("Simulate AI Camera Scan")
        btn_sim.clicked.connect(self.run_ai_scan)
        
        sb_layout.addWidget(self.res_lbl)
        sb_layout.addWidget(btn_sim)
        
        layout.addWidget(scan_box)
        layout.addStretch()
        return page

    def run_ai_scan(self):
        self.res_lbl.setText("Scanning...")
        QTimer.singleShot(800, lambda: self.res_lbl.setText(
            "<b>Book Found:</b> HC Verma — Concepts of Physics Vol 1<br>"
            "<b>Author:</b> H.C. Verma | <b>Est. Price:</b> ₹320 - ₹420"
        ))

    # PAGE 3: EXCHANGE
    def create_exchange_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        title = QLabel("🔄 Smart Exchange Engine")
        title.setStyleSheet("font-size: 22px; font-weight: bold;")
        
        have_input = QLineEdit("Mathematics Class 12 - NCERT")
        want_input = QLineEdit("Physics Part 1 Class 11 - NCERT")
        
        btn_match = QPushButton("Find Graph Matches")
        btn_match.clicked.connect(lambda: QMessageBox.information(self, "Match", "3 Direct Matches Found in Laxmi Nagar!"))
        
        layout.addWidget(title)
        layout.addWidget(QLabel("YOU HAVE:"))
        layout.addWidget(have_input)
        layout.addWidget(QLabel("YOU WANT:"))
        layout.addWidget(want_input)
        layout.addWidget(btn_match)
        layout.addStretch()
        return page

    # PAGE 4: SAFETY
    def create_safety_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.addWidget(QLabel("🛡️ Trust & Safety Hub"))
        layout.addWidget(QLabel("• Verified Student Profiles via School Email\n• Privacy by Design (Location hidden)\n• Secure In-App Chat"))
        layout.addStretch()
        return page

    # PAGE 5: ESG DASHBOARD
    def create_esg_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.addWidget(QLabel("🌱 Personal Impact Dashboard"))
        layout.addWidget(QLabel("• Impact Points: 1,250\n• Books Reused: 42\n• CO2e Emissions Avoided: 98.4 kg"))
        layout.addStretch()
        return page

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShioriApp()
    window.show()
    sys.argv.append('--style=Fusion')
    sys.exit(app.exec())
