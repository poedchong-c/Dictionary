import flet as ft
import requests

API_URL = "http://127.0.0.1:8000"

def main(page: ft.Page):
    page.title = "Sign Language Dictionary"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 600
    page.window_height = 800
    page.bgcolor = "#E8F4FE"
    page.scroll = "auto"
    
    current_page = {"page": "login"}
    selected_category = {"name": None}
    selected_word = {"item": None}

    categories_data = {
        "คำทักทาย": [
            {"word": "สวัสดี", "meaning": "Hello", "gif": "https://www.th-sl.com//wp-content/uploads/2020/09/1.1.1.gif"},
            {"word": "ขอบคุณ", "meaning": "Thank you", "gif": "https://www.th-sl.com//wp-content/uploads/2020/09/1.2.1.gif"},
            {"word": "สบายดี", "meaning": "I am fine", "gif": "https://www.th-sl.com//wp-content/uploads/2021/10/4.098.gif"},
            {"word": "ยินดีด้วย", "meaning": "Welcome", "gif": "https://www.th-sl.com//wp-content/uploads/2023/12/2566-0945.gif"}
        ],
        "คำถาม": [
            {"word": "ทำไม", "meaning": "Why", "gif": "https://www.th-sl.com//wp-content/uploads/2020/09/1.56.1.gif"},
            {"word": "กี่โมง", "meaning": "What time", "gif": "https://www.th-sl.com//wp-content/uploads/2021/10/6.041-02.gif"},
            {"word": "อะไร", "meaning": "What", "gif": "https://www.th-sl.com//wp-content/uploads/2020/09/1.55.1.gif"}
        ],
        "ตัวเลข": [
            {"word": "หนึ่ง", "meaning": "One", "gif": "https://www.th-sl.com//wp-content/uploads/2021/05/2.100.1.gif"},
            {"word": "สอง", "meaning": "Two", "gif": "https://www.th-sl.com//wp-content/uploads/2021/05/2.100.2.gif"},
            {"word": "สาม", "meaning": "Three", "gif": "https://www.th-sl.com//wp-content/uploads/2021/05/2.100.3.gif"},
            {"word": "สี่", "meaning": "Four", "gif": "https://www.th-sl.com//wp-content/uploads/2021/05/2.100.4.gif"},
            {"word": "ห้า", "meaning": "Five", "gif": "https://www.th-sl.com//wp-content/uploads/2021/05/2.100.5.gif"},
        ],
        "เวลา": [
            {"word": "ตอนเช้า", "meaning": "Morning", "gif": "https://www.th-sl.com//wp-content/uploads/2020/09/1.35.2.gif"},
            {"word": "ตอนเย็น", "meaning": "Evening", "gif": "https://www.th-sl.com//wp-content/uploads/2020/09/1.37.1.gif"},
            {"word": "เที่ยงวัน", "meaning": "Noon", "gif": "https://www.th-sl.com//wp-content/uploads/2021/06/2.100.47.gif"},
            {"word": "เที่ยงคืน", "meaning": "Midnight", "gif": "https://www.th-sl.com//wp-content/uploads/2025/06/1.38.2-2.gif"},
        ],
        "อารมณ์": [
            {"word": "หมั่นไส้", "meaning": "dislike", "gif": "https://www.th-sl.com//wp-content/uploads/2025/11/2568-0383.gif"},
            {"word": "เบื่อ", "meaning": "bored", "gif": "https://www.th-sl.com//wp-content/uploads/2020/09/5.87.1.gif"},
            {"word": "โกรธ", "meaning": "angry", "gif": "https://www.th-sl.com//wp-content/uploads/2020/09/5.72.1.gif"},
            {"word": "เสียใจ", "meaning": "sad", "gif": "https://www.th-sl.com//wp-content/uploads/2020/09/5.83.2.gif"},
            {"word": "ดีใจ", "meaning": "happy", "gif": "https://www.th-sl.com//wp-content/uploads/2020/09/5.83.1.gif"}
        ],
        "อาหาร": [
            {"word": "ข้าวไก่ทอด", "meaning": "fried chicken rice", "gif": "https://www.th-sl.com//wp-content/uploads/2025/08/2568-0295.gif"},
            {"word": "กะเพรา", "meaning": "kaphra", "gif": "https://www.th-sl.com//wp-content/uploads/2020/09/3.13.2.gif"},
            {"word": "ไข่เจียว", "meaning": "omelette", "gif": "https://www.th-sl.com//wp-content/uploads/2023/11/5-4-1.gif"},
            {"word": "ผัดไทย", "meaning": "pad thai", "gif": "https://www.th-sl.com//wp-content/uploads/2020/09/5.15.2.gif"},
        ]
    }

    # ✅ FIXED DIALOG
    def show_gif_dialog(gif_url, title):
        import webbrowser

        def close_dialog(e):
            if hasattr(page, 'close'):
                page.close(dlg)
            else:
                page.dialog.open = False
                page.update()

        def open_in_browser(e):
            webbrowser.open(gif_url)

        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text(title, size=18, weight="bold", color="#0277BD"),
            content=ft.Container(
                content=ft.Column([
                    ft.Image(src=gif_url, width=250, height=250),
                    ft.Text("🌐 GIF from Tenor", size=10, color="#888"),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                width=300,
                height=350,
                padding=20,
            ),
            actions=[
                ft.TextButton("Browser", on_click=open_in_browser),
                ft.Button("Close", on_click=close_dialog),
            ],
        )

        if hasattr(page, 'open'):
            page.open(dlg)
        else:
            page.dialog = dlg
            page.dialog.open = True
            page.update()

    def show_page(page_name, **kwargs):
        current_page["page"] = page_name
        page.clean()
        
        if page_name == "login":
            email = ft.TextField(
                label="Username",
                width=300,
                bgcolor="white",
                border_color="#E0E0E0",
                filled=True,
                content_padding=12
            )
            password = ft.TextField(
                label="Password",
                password=True,
                width=300,
                bgcolor="white",
                border_color="#E0E0E0",
                filled=True,
                content_padding=12
            )
            
            show_password_checkbox = ft.Checkbox(
                label="Show Password",
                value=False,
                on_change=lambda e: toggle_password()
            )

            def toggle_password():
                password.password = not show_password_checkbox.value
                page.update()

            def login(e):
                if email.value and password.value:
                    show_page("home")

            def forgot_password(e):
                pass  # Implement forgot password functionality

            def create_account(e):
                show_page("register")

            login_form = ft.Container(
                content=ft.Column([
                    ft.Text("Sign In", size=32, weight="bold", color="#1F1F1F"),
                    ft.Text("sign in to your account", size=14, color="#666666"),
                    ft.Divider(height=20, color="transparent"),
                    
                    email,
                    ft.Divider(height=10, color="transparent"),
                    
                    password,
                    ft.Divider(height=10, color="transparent"),
                    
                    ft.Row([
                        show_password_checkbox,
                        ft.TextButton("Forgot?", on_click=forgot_password, style=ft.ButtonStyle(color="#1976D2"))
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, width=300),
                    ft.Divider(height=15, color="transparent"),
                    
                    ft.Button(
                        "Sign In",
                        width=300,
                        height=45,
                        on_click=login,
                        style=ft.ButtonStyle(
                            bgcolor="#1976D2",
                            color="white",
                            shape=ft.RoundedRectangleBorder(radius=5)
                        )
                    ),
                    ft.Divider(height=15, color="transparent"),
                    
                    ft.Row([
                        ft.Text("Don't have an account? ", color="#666666"),
                        ft.TextButton("Register", on_click=create_account, style=ft.ButtonStyle(color="#1976D2"))
                    ], alignment=ft.MainAxisAlignment.CENTER)
                ], width=320, spacing=0, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=40,
                border_radius=8,
                bgcolor="white",
                shadow=ft.BoxShadow(blur_radius=10, color="#00000015")
            )

            page.add(
                ft.Column([
                    login_form
                ], alignment=ft.MainAxisAlignment.CENTER,
                   horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                   expand=True)
            )

        elif page_name == "register":
            username_reg = ft.TextField(
                label="Username",
                width=300,
                bgcolor="white",
                border_color="#E0E0E0",
                filled=True,
                content_padding=12
            )
            password_reg = ft.TextField(
                label="Password",
                password=True,
                width=300,
                bgcolor="white",
                border_color="#E0E0E0",
                filled=True,
                content_padding=12
            )
            confirm_password_reg = ft.TextField(
                label="Confirm Password",
                password=True,
                width=300,
                bgcolor="white",
                border_color="#E0E0E0",
                filled=True,
                content_padding=12
            )

            show_passwords_reg_checkbox = ft.Checkbox(
                label="Show Password",
                value=False,
                on_change=lambda e: toggle_passwords_reg()
            )

            def toggle_passwords_reg():
                password_reg.password = not show_passwords_reg_checkbox.value
                confirm_password_reg.password = not show_passwords_reg_checkbox.value
                page.update()

            error_message = ft.Text("", color="red", size=12)

            def register(e):
                if not username_reg.value:
                    error_message.value = "Username is required"
                    page.update()
                    return
                if not password_reg.value:
                    error_message.value = "Password is required"
                    page.update()
                    return
                if password_reg.value != confirm_password_reg.value:
                    error_message.value = "Passwords do not match"
                    page.update()
                    return
                    
                # Here you can add registration API call
                error_message.value = ""
                show_page("login")

            register_form = ft.Container(
                content=ft.Column([
                    ft.Text("Create Account", size=32, weight="bold", color="#1F1F1F"),
                    ft.Text("Register a new account", size=14, color="#666666"),
                    ft.Divider(height=20, color="transparent"),
                    
                    username_reg,
                    ft.Divider(height=10, color="transparent"),
                    
                    password_reg,
                    ft.Divider(height=10, color="transparent"),
                    
                    confirm_password_reg,
                    ft.Divider(height=10, color="transparent"),
                    
                    ft.Row([
                        show_passwords_reg_checkbox,
                        ft.Text("", size=14)
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, width=300),
                    ft.Divider(height=8, color="transparent"),
                    
                    error_message,
                    ft.Divider(height=15, color="transparent"),
                    
                    ft.Button(
                        "Register",
                        width=300,
                        height=45,
                        on_click=register,
                        style=ft.ButtonStyle(
                            bgcolor="#1976D2",
                            color="white",
                            shape=ft.RoundedRectangleBorder(radius=5)
                        )
                    ),
                    ft.Divider(height=15, color="transparent"),
                    
                    ft.Button(
                        "Back to Sign In",
                        width=300,
                        height=45,
                        on_click=lambda e: show_page("login"),
                        style=ft.ButtonStyle(
                            bgcolor="#FFFFFF",
                            color="#1976D2",
                            shape=ft.RoundedRectangleBorder(radius=5)
                        )
                    )
                ], width=320, spacing=0, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=40,
                border_radius=8,
                bgcolor="white",
                shadow=ft.BoxShadow(blur_radius=10, color="#00000015")
            )

            page.add(
                ft.Column([
                    register_form
                ], alignment=ft.MainAxisAlignment.CENTER,
                   horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                   expand=True)
            )

        elif page_name == "home":
            search_text = ft.TextField(
                hint_text="ค้นหาคำศัพท์",
                width=260,
                on_change=lambda e: filter_words(e.control.value),
                on_submit=lambda e: filter_words(e.control.value),
                filled=True,
                border_color="#B3D7FF",
                bgcolor="#FFFFFF",
                content_padding=12
            )

            category_buttons = ft.GridView(
                expand=False,
                max_extent=140,
                child_aspect_ratio=1,
                spacing=10,
                run_spacing=10
            )

            def goto_category(cat_name):
                selected_category["name"] = cat_name
                show_page("category")

            for cat_name in ["คำทักทาย", "คำถาม", "ตัวเลข", "เวลา", "อารมณ์", "อาหาร"]:
                category_buttons.controls.append(
                    ft.Button(
                        cat_name,
                        width=120,
                        height=120,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor="#1976D2",
                            color="white"
                        ),
                        on_click=lambda e, n=cat_name: goto_category(n)
                    )
                )

            search_results = ft.Column(spacing=0)
            search_panel = ft.Container(
                visible=False,
                width=420,
                top=122,
                left=40,
                border_radius=10,
                bgcolor="#FFFFFF",
                border=ft.border.all(1, "#E0E0E0"),
                shadow=ft.BoxShadow(blur_radius=12, color="#00000020"),
                content=search_results
            )

            def filter_words(query):
                q = query.strip().lower()
                search_results.controls.clear()

                if q == "":
                    search_panel.visible = False
                    page.update()
                    return

                for cat, words in categories_data.items():
                    for item in words:
                        if q in item["word"].lower() or q in item["meaning"].lower():
                            search_results.controls.append(
                                ft.GestureDetector(
                                    on_tap=lambda e, w=item: show_page("word", word_item=w),
                                    content=ft.Container(
                                        width=420,
                                        padding=ft.padding.only(top=8, bottom=8, left=12, right=12),
                                        bgcolor="#FFFFFF",
                                        content=ft.Text(item["word"], size=16, weight="bold", color="#1F1F1F")
                                    )
                                )
                            )

                if not search_results.controls:
                    search_results.controls.append(ft.Text("ไม่พบคำศัพท์ที่ตรงกับคำค้นหา", size=14, color="#888888", padding=10))

                search_panel.visible = True
                page.update()

            def clear_search(e):
                search_text.value = ""
                search_results.controls.clear()
                search_panel.visible = False
                page.update()

            home_body = ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text("พจนานุกรมภาษามือ", size=28, weight="bold", color="#1F1F1F"),
                    ], alignment=ft.MainAxisAlignment.START),
                    ft.Divider(height=10, color="transparent"),
                    
                    ft.Row([
                        search_text
                    ], alignment=ft.MainAxisAlignment.START),
                    
                    ft.Divider(height=15, color="transparent"),
                    ft.Text("หมวดหมู่คำใช้บ่อย", size=18, weight="bold", color="#1F1F1F"),
                    ft.Divider(height=10, color="transparent"),
                    category_buttons
                ], expand=True),
                padding=20,
                width=500,
                bgcolor="#FFFFFF",
                border_radius=10,
                shadow=ft.BoxShadow(blur_radius=20, color="#00000020")
            )

            page.add(
                ft.Stack(
                    width=500,
                    height=700,
                    controls=[
                        home_body,
                        search_panel
                    ]
                )
            )

        elif page_name == "category":
            cat_name = selected_category.get("name")
            words = categories_data.get(cat_name, [])

            # ✅ 3. ฟังก์ชันและ Dialog สำหรับเพิ่มคำศัพท์ใหม่เข้ามาในหมวดหมู่
            def open_add_word_dialog(e):
                new_word_input = ft.TextField(label="คำศัพท์", width=300, autofocus=True)
                new_meaning_input = ft.TextField(label="ความหมาย", width=300)
                new_gif_input = ft.TextField(label="GIF URL", width=300)

                # สร้าง Dialog แยกไว้ก่อน
                dlg = ft.AlertDialog(
                    modal=True,
                    title=ft.Text(f"เพิ่มคำศัพท์ใหม่ (หมวด: {cat_name})", size=18, weight="bold"),
                    content=ft.Column([new_word_input, new_meaning_input, new_gif_input], tight=True)
                )

                def save_new_word(e):
                    if new_word_input.value:
                        words.append({
                            "word": new_word_input.value,
                            "meaning": new_meaning_input.value,
                            "gif": new_gif_input.value or "https://media.tenor.com/h_Z5bfUZTfgAAAAM/penguin-hello.gif"
                        })
                        
                        # ปิด Dialog ให้ถูกวิธีตาม Flet เวอร์ชั่นใหม่
                        if hasattr(page, 'close'):
                            page.close(dlg)
                        else:
                            dlg.open = False
                            page.update()
                            
                        show_page("category") # โหลดหน้าใหม่เพื่อให้ปุ่มแสดงผล
                    else:
                        # ถ้าไม่ยอมพิมพ์คำศัพท์ ให้ขึ้นเตือนแดงๆ
                        new_word_input.error_text = "กรุณากรอกคำศัพท์ก่อนบันทึกโว้ย!"
                        page.update()

                def close_dialog(e):
                    if hasattr(page, 'close'):
                        page.close(dlg)
                    else:
                        dlg.open = False
                        page.update()

                # ใส่ปุ่ม Action ให้ Dialog
                dlg.actions = [
                    ft.TextButton("บันทึก", on_click=save_new_word),
                    ft.TextButton("ยกเลิก", on_click=close_dialog)
                ]

                # เปิด Dialog ให้ถูกวิธีตาม Flet เวอร์ชั่นใหม่
                if hasattr(page, 'open'):
                    page.open(dlg)
                else:
                    page.dialog = dlg
                    dlg.open = True
                    page.update()

            page.add(
                ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Row([
                                ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=lambda e: show_page("home")),
                                ft.Text(cat_name, size=24, weight="bold", color="#1F1F1F")
                            ]),
                            ft.IconButton(icon=ft.Icons.ADD_CIRCLE, icon_size=32, icon_color="#1976D2", tooltip="เพิ่มคำศัพท์", on_click=open_add_word_dialog)
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Divider(height=10, color="transparent"),
                        ft.GridView(
                            expand=False,
                            max_extent=140,
                            child_aspect_ratio=1,
                            spacing=10,
                            run_spacing=10,
                            controls=[
                                ft.Button(
                                    item["word"],
                                    width=120,
                                    height=120,
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                        bgcolor="#1976D2",
                                        color="white"
                                    ),
                                    on_click=lambda e, w=item: show_page("word", word_item=w)
                                )
                                for item in words
                            ]
                        )
                    ], expand=True),
                    padding=20,
                    width=500,
                    bgcolor="#FFFFFF",
                    border_radius=10,
                    shadow=ft.BoxShadow(blur_radius=20, color="#00000020")
                )
            )

        elif page_name == "word":
            word_item = kwargs.get("word_item")
            if not word_item:
                word_item = selected_word.get("item")

            if not word_item:
                page.add(ft.Text("ไม่พบคำศัพท์", size=18, color="red"))
                return

            selected_word["item"] = word_item

            page.add(
                ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=lambda e: show_page("category")),
                            ft.Text(word_item["word"], size=24, weight="bold", color="#1F1F1F")
                        ], alignment=ft.MainAxisAlignment.START),
                        ft.Divider(height=15, color="transparent"),
                        ft.Image(src=word_item.get("gif", "https://media.tenor.com/h_Z5bfUZTfgAAAAM/penguin-hello.gif"), width=320, height=220),
                        ft.Divider(height=10, color="transparent"),
                        ft.Text(word_item["word"], size=22, weight="bold"),
                        ft.Text(word_item.get("meaning", ""), size=16, color="#555555"),
                        ft.Divider(height=20, color="transparent"),
                        ft.Button("กลับ", width=300, on_click=lambda e: show_page("category"), style=ft.ButtonStyle(bgcolor="#1976D2", color="white", shape=ft.RoundedRectangleBorder(radius=10)))
                    ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True),
                    padding=20,
                    width=500,
                    bgcolor="#FFFFFF",
                    border_radius=10,
                    shadow=ft.BoxShadow(blur_radius=20, color="#00000020")
                )
            )

        elif page_name == "add":
            word_input = ft.TextField(label="Word")
            meaning_input = ft.TextField(label="Meaning")
            gif_input = ft.TextField(label="GIF URL")
            category_input = ft.TextField(label="Category ID")

            def add_word(e):
                data = {
                    "word": word_input.value,
                    "meaning": meaning_input.value,
                    "gif_url": gif_input.value,
                    "category_id": int(category_input.value)
                }
                # ถ้า API ยังไม่พร้อมใช้งาน ส่วนนี้อาจจะ error ได้นะครับ
                try:
                    requests.post(f"{API_URL}/words", json=data)
                except Exception as ex:
                    print(f"API Error: {ex}")
                show_page("home")

            page.add(
                ft.Column([
                    ft.Text("Add Word", size=25),
                    word_input,
                    meaning_input,
                    gif_input,
                    category_input,

                    ft.Button("Save", on_click=add_word),
                    ft.TextButton("Back", on_click=lambda e: show_page("home"))
                ], expand=True)
            )

    show_page("login")

ft.app(target=main)