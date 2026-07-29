#!/usr/bin/env python3
"""
TOTP 验证码生成器
依赖: pip install pyotp
"""

import tkinter as tk
import pyotp
import time
import platform
import webbrowser


def enable_dpi_awareness():
    if platform.system() == "Windows":
        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(2)
        except Exception:
            try:
                windll.user32.SetProcessDPIAware()
            except Exception:
                pass


def sys_font(size, bold=False):
    w = "bold" if bold else "normal"
    if platform.system() == "Darwin":  return ("SF Pro Text",       size, w)
    if platform.system() == "Windows": return ("Segoe UI",           size, w)
    return ("Ubuntu", size, w)

def mono_font(size, bold=False):
    w = "bold" if bold else "normal"
    if platform.system() == "Darwin":  return ("SF Mono",            size, w)
    if platform.system() == "Windows": return ("Consolas",           size, w)
    return ("DejaVu Sans Mono", size, w)


class TOTPApp:
    BG     = "#F6F6F4"
    CARD   = "#FFFFFF"
    ACCENT = "#111111"
    MUTED  = "#AAAAAA"
    BORDER = "#E4E4E0"
    DANGER = "#C94B1F"
    GREEN  = "#2A7A46"
    BAR_BG = "#E4E4E0"

    W, H = 460, 400

    def __init__(self, root: tk.Tk):
        self.root = root
        self._setup_window()
        self._build_ui()
        self._tick()

    def _setup_window(self):
        self.root.title("TOTP")
        self.root.configure(bg=self.BG)
        self.root.resizable(False, False)

        # ====== 新增菜单栏 ======
        menu_bar = tk.Menu(self.root)
        about_menu = tk.Menu(menu_bar, tearoff=0)
        about_menu.add_command(label="关于作者 蔡Tony", command=self._show_about_window)
        menu_bar.add_cascade(label="关于", menu=about_menu)
        self.root.config(menu=menu_bar)
        # =========================

        if platform.system() == "Darwin":
            try: self.root.tk.call("tk", "scaling", 2.0)
            except Exception: pass
        self.root.geometry(f"{self.W}x{self.H}")
        self.root.update_idletasks()
        sx, sy = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry(f"{self.W}x{self.H}+{(sx-self.W)//2}+{(sy-self.H)//2}")

    def _show_about_window(self):
        # 创建独立的关于弹窗
        about_win = tk.Toplevel(self.root)
        about_win.title("关于作者")
        about_win.geometry("320x210")
        about_win.configure(bg=self.BG)
        about_win.resizable(False, False)
        
        # 让弹窗相对主窗口居中
        about_win.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() // 2) - (320 // 2)
        y = self.root.winfo_y() + (self.root.winfo_height() // 2) - (210 // 2)
        about_win.geometry(f"+{x}+{y}")
        
        outer = tk.Frame(about_win, bg=self.BG)
        outer.pack(fill="both", expand=True, padx=24, pady=24)
        
        # 模仿主界面的卡片设计
        card = tk.Frame(outer, bg=self.CARD, highlightbackground=self.BORDER, highlightthickness=1)
        card.pack(fill="both", expand=True)
        
        inner = tk.Frame(card, bg=self.CARD)
        inner.pack(fill="both", expand=True, padx=16, pady=20)
        
        # 开发者信息 (采用应用统一的字体系统)
        tk.Label(inner, text="蔡Tony", font=sys_font(14, bold=True), bg=self.CARD, fg=self.ACCENT).pack(pady=(0, 4))
        tk.Label(inner, text="走在成长的路上，不断探索", font=sys_font(10), bg=self.CARD, fg=self.MUTED).pack(pady=(0, 20))
        
        # 可点击的超链接区域
        link_frame = tk.Frame(inner, bg=self.CARD)
        link_frame.pack()
        
        tk.Label(link_frame, text="网站主页: ", font=sys_font(10), bg=self.CARD, fg=self.ACCENT).pack(side="left")
        
        link_lbl = tk.Label(link_frame, text="蔡Tony的空间", font=sys_font(10, bold=True), fg="#2962FF", bg=self.CARD, cursor="hand2")
        link_lbl.pack(side="left")
        
        # 增加悬停反馈
        link_lbl.bind("<Enter>", lambda e: link_lbl.config(fg="#0039CB"))
        link_lbl.bind("<Leave>", lambda e: link_lbl.config(fg="#2962FF"))
        # 绑定左键点击事件打开网页
        link_lbl.bind("<Button-1>", lambda e: webbrowser.open_new("https://caitony.dpdns.org/"))

    def _build_ui(self):
        P = 28  # 水平 padding
        outer = tk.Frame(self.root, bg=self.BG)
        outer.pack(fill="both", expand=True, padx=P, pady=24)

        # 标题
        tk.Label(outer, text="TOTP 验证码生成器",
                 bg=self.BG, fg=self.ACCENT,
                 font=sys_font(16, bold=True), anchor="w").pack(fill="x")

        # 密钥输入
        tk.Label(outer, text="密钥",
                 bg=self.BG, fg=self.MUTED,
                 font=sys_font(10), anchor="w").pack(fill="x", pady=(18, 4))

        entry_frame = tk.Frame(outer, bg=self.CARD,
                               highlightbackground=self.BORDER, highlightthickness=1)
        entry_frame.pack(fill="x")

        self.secret_var = tk.StringVar()
        self.secret_var.trace_add("write", lambda *_: None)

        self.entry = tk.Entry(
            entry_frame, textvariable=self.secret_var,
            font=mono_font(12), bg=self.CARD, fg=self.ACCENT,
            insertbackground=self.ACCENT, relief="flat", bd=0,
        )
        self.entry.pack(fill="x", padx=12, ipady=9)
        self.entry.focus_set()

        # 错误提示（固定占位）
        self.error_var = tk.StringVar(value=" ")
        tk.Label(outer, textvariable=self.error_var,
                 bg=self.BG, fg=self.DANGER,
                 font=sys_font(9), anchor="w").pack(fill="x", pady=(4, 0))

        # 验证码卡片
        card = tk.Frame(outer, bg=self.CARD,
                        highlightbackground=self.BORDER, highlightthickness=1)
        card.pack(fill="x", pady=(10, 0))

        inner = tk.Frame(card, bg=self.CARD)
        inner.pack(fill="x", padx=18, pady=18)

        # 验证码 + 复制按钮
        row = tk.Frame(inner, bg=self.CARD)
        row.pack(fill="x")

        self.code_var = tk.StringVar(value="———  ———")
        self.code_lbl = tk.Label(row, textvariable=self.code_var,
                                 font=mono_font(34, bold=True),
                                 fg=self.MUTED, bg=self.CARD, anchor="w")
        self.code_lbl.pack(side="left")

        self.copy_btn = tk.Button(
            row, text="复制", command=self._copy,
            font=sys_font(10), bg=self.BG, fg=self.ACCENT,
            relief="flat", bd=0, padx=12, pady=6, cursor="hand2",
            activebackground=self.BORDER, activeforeground=self.ACCENT,
            highlightbackground=self.BORDER, highlightthickness=1,
        )
        self.copy_btn.pack(side="right", anchor="center")

        # ── 进度条（Canvas 实现，宽度精准可控）──
        self._bar_canvas = tk.Canvas(
            inner, height=5, bg=self.BAR_BG,
            highlightthickness=0, bd=0,
        )
        self._bar_canvas.pack(fill="x", pady=(14, 8))
        # 等 Canvas 渲染后再画矩形
        self._bar_rect = None
        self._bar_canvas.bind("<Configure>", self._on_bar_resize)

        # 倒计时 + 下一个
        foot = tk.Frame(inner, bg=self.CARD)
        foot.pack(fill="x")

        self.cd_var = tk.StringVar(value="")
        self._cd_lbl = tk.Label(foot, textvariable=self.cd_var,
                                font=sys_font(10, bold=True),
                                fg=self.MUTED, bg=self.CARD, anchor="w")
        self._cd_lbl.pack(side="left")

        nw = tk.Frame(foot, bg=self.CARD)
        nw.pack(side="right")
        tk.Label(nw, text="下一个", bg=self.CARD, fg=self.MUTED,
                 font=sys_font(9)).pack(side="left", padx=(0, 6))
        self.next_var = tk.StringVar(value="——————")
        tk.Label(nw, textvariable=self.next_var, bg=self.CARD, fg=self.MUTED,
                 font=mono_font(12, bold=True)).pack(side="left")

    def _on_bar_resize(self, event):
        """Canvas 尺寸变化时重建矩形"""
        self._draw_bar(self._last_pct if hasattr(self, "_last_pct") else 1.0,
                       self._last_danger if hasattr(self, "_last_danger") else False)

    def _draw_bar(self, pct: float, danger: bool):
        self._last_pct    = pct
        self._last_danger = danger
        c = self._bar_canvas
        w = c.winfo_width()
        h = c.winfo_height()
        if w <= 1:
            return
        c.delete("bar")
        color = self.DANGER if danger else self.ACCENT
        fill_w = max(int(w * pct), 0)
        if fill_w > 0:
            c.create_rectangle(0, 0, fill_w, h, fill=color, outline="", tags="bar")

    def _get_totp(self, secret: str, offset: int = 0) -> str:
        cleaned = secret.replace(" ", "").upper()
        cleaned += "=" * ((8 - len(cleaned) % 8) % 8)
        ts = int(time.time()) // 30 + offset
        return pyotp.TOTP(cleaned).at(ts * 30)

    def _tick(self):
        now       = int(time.time())
        remaining = 30 - now % 30
        pct       = remaining / 30
        danger    = remaining <= 7
        secret    = self.secret_var.get().strip()

        if secret:
            try:
                code = self._get_totp(secret)
                nxt  = self._get_totp(secret, 1)
                self.error_var.set(" ")
                self.code_var.set(f"{code[:3]}  {code[3:]}")
                self.code_lbl.config(fg=self.ACCENT)
                self.next_var.set(f"{nxt[:3]} {nxt[3:]}")
                self.cd_var.set(f"{'⚠  ' if danger else ''}{remaining}s")
                self._cd_lbl.config(fg=self.DANGER if danger else self.MUTED)
            except Exception as e:
                self.error_var.set(f"⚠ 密钥无效：{e}")
                self.code_var.set("———  ———")
                self.code_lbl.config(fg=self.MUTED)
                self.next_var.set("——————")
                self.cd_var.set("")
                pct = 0
        else:
            self.error_var.set(" ")
            self.code_var.set("———  ———")
            self.code_lbl.config(fg=self.MUTED)
            self.next_var.set("——————")
            self.cd_var.set("")

        self._draw_bar(pct, danger)
        self.root.after(300, self._tick)

    def _copy(self):
        raw = self.code_var.get().replace(" ", "")
        if not raw or "—" in raw:
            return
        self.root.clipboard_clear()
        self.root.clipboard_append(raw)
        self.copy_btn.config(text="✓ 已复制", fg=self.GREEN)
        self.root.after(1800, lambda: self.copy_btn.config(text="复制", fg=self.ACCENT))


if __name__ == "__main__":
    enable_dpi_awareness()
    root = tk.Tk()
    try:
        dpi = root.winfo_fpixels("1i")
        if dpi / 72.0 > 1.2:
            root.tk.call("tk", "scaling", dpi / 72.0)
    except Exception:
        pass
    TOTPApp(root)
    root.mainloop()
