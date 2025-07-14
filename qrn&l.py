import qrcode
import os

try:
    from PIL import Image, ImageDraw, ImageFont

    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    print("PIL not available. Basic QR codes will still work.")

try:
    import qrcode.image.styledpil
    from qrcode.image.styledpil import StyledPilImage
    from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, SquareModuleDrawer, CircleModuleDrawer

    STYLED_QR_AVAILABLE = True
except ImportError:
    STYLED_QR_AVAILABLE = False
    print("Styled QR features not available. Using basic QR codes.")


def generate_basic_qr():
    """Generate a basic black and white QR code"""
    url = "https://github.com/ShivamJhuria/python-/blob/main/snakandladders.py"

    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # Size of each box in pixels
        border=4,  # Size of the border
    )

    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save("snake_ladder_basic_qr.png")
    print("✅ Basic QR code saved as 'snake_ladder_basic_qr.png'")
    return img


def generate_styled_qr():
    """Generate a styled QR code with colors"""
    url = "https://github.com/ShivamJhuria/python-/blob/main/snakandladders.py"

    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    if STYLED_QR_AVAILABLE:
        try:
            # Create styled image with rounded corners
            img = qr.make_image(
                image_factory=StyledPilImage,
                module_drawer=RoundedModuleDrawer(),
                fill_color=(34, 139, 34),  # Forest green
                back_color=(255, 255, 255)  # White background
            )
        except Exception as e:
            print(f"⚠️ Styled QR failed, using colored QR: {e}")
            # Fallback to basic colored QR
            img = qr.make_image(fill_color=(34, 139, 34), back_color="white")
    else:
        # Basic colored QR code
        img = qr.make_image(fill_color="darkgreen", back_color="white")

    img.save("snake_ladder_styled_qr.png")
    print("✅ Styled QR code saved as 'snake_ladder_styled_qr.png'")
    return img


def generate_game_themed_qr():
    """Generate a game-themed QR code"""
    url = "https://github.com/ShivamJhuria/python-/blob/main/snakandladders.py"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    if STYLED_QR_AVAILABLE:
        try:
            # Snake and ladder themed colors
            img = qr.make_image(
                image_factory=StyledPilImage,
                module_drawer=CircleModuleDrawer(),
                fill_color=(139, 69, 19),  # Brown color (like wooden ladder)
                back_color=(240, 248, 255)  # Light blue background
            )
        except Exception as e:
            print(f"⚠️ Themed QR failed, using colored QR: {e}")
            # Fallback to basic colored QR
            img = qr.make_image(fill_color=(139, 69, 19), back_color=(240, 248, 255))
    else:
        # Basic colored QR code
        img = qr.make_image(fill_color="saddlebrown", back_color="lightblue")

    img.save("snake_ladder_themed_qr.png")
    print("✅ Game-themed QR code saved as 'snake_ladder_themed_qr.png'")
    return img


def generate_high_contrast_qr():
    """Generate a high contrast QR code for better readability"""
    url = "https://github.com/ShivamJhuria/python-/blob/main/snakandladders.py"

    qr = qrcode.QRCode(
        version=2,  # Slightly larger version for better readability
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=8,
        border=6,
    )

    qr.add_data(url)
    qr.make(fit=True)

    # High contrast colors
    img = qr.make_image(fill_color="black", back_color="white")

    img.save("snake_ladder_high_contrast_qr.png")
    print("✅ High contrast QR code saved as 'snake_ladder_high_contrast_qr.png'")
    return img


def add_logo_to_qr(qr_img, logo_path=None):
    """Add a logo to the center of the QR code"""
    if not PIL_AVAILABLE:
        print("⚠️ PIL not available. Cannot add logo to QR code.")
        return qr_img

    if logo_path and os.path.exists(logo_path):
        try:
            logo = Image.open(logo_path)

            # Calculate logo size (should be about 1/5 of QR code size)
            qr_width, qr_height = qr_img.size
            logo_size = min(qr_width, qr_height) // 5

            # Resize logo
            logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

            # Create a white background for the logo
            logo_bg = Image.new('RGB', (logo_size + 20, logo_size + 20), 'white')
            logo_pos = ((logo_bg.width - logo.width) // 2, (logo_bg.height - logo.height) // 2)
            logo_bg.paste(logo, logo_pos)

            # Paste logo onto QR code
            qr_pos = ((qr_width - logo_bg.width) // 2, (qr_height - logo_bg.height) // 2)
            qr_img.paste(logo_bg, qr_pos)

            return qr_img
        except Exception as e:
            print(f"⚠️ Could not add logo: {e}")
            return qr_img
    else:
        return qr_img


def generate_all_qr_codes():
    """Generate all variations of QR codes"""
    print("🎮 Generating QR codes for Snake and Ladder Game")
    print("🔗 URL: https://github.com/ShivamJhuria/python-/blob/main/snakandladders.py")
    print("-" * 60)

    # Generate different styles
    generate_basic_qr()
    generate_styled_qr()
    generate_game_themed_qr()
    generate_high_contrast_qr()

    print("-" * 60)
    print("✨ All QR codes generated successfully!")
    print("\n📱 How to use:")
    print("1. Open any QR code scanner app on your phone")
    print("2. Point the camera at any of the generated QR codes")
    print("3. Tap the link to view your Snake and Ladder game code")
    print("\n🎯 Recommended for printing: 'snake_ladder_high_contrast_qr.png'")
    print("🎨 Recommended for digital sharing: 'snake_ladder_styled_qr.png'")


def test_qr_code():
    """Test function to verify QR code works"""
    try:
        import cv2
        print("\n🔍 Testing QR code readability...")

        # Try to read the basic QR code
        img = cv2.imread("snake_ladder_basic_qr.png")
        if img is not None:
            detector = cv2.QRCodeDetector()
            data, vertices_array, binary_qrcode = detector.detectAndDecode(img)

            if data:
                print(f"✅ QR code is readable! Detected URL: {data}")
            else:
                print("❌ QR code could not be read")
        else:
            print("❌ Could not load QR code image for testing")

    except ImportError:
        print("💡 Install opencv-python to test QR code readability:")
        print("   pip install opencv-python")
    except Exception as e:
        print(f"⚠️ Error testing QR code: {e}")


def create_simple_qr():
    """Create a simple QR code without any styling dependencies"""
    url = "https://github.com/ShivamJhuria/python-/blob/main/snakandladders.py"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("simple_snake_ladder_qr.png")
    print("✅ Simple QR code saved as 'simple_snake_ladder_qr.png'")
    return img


if __name__ == "__main__":
    print("🎮 QR Code Generator for Snake and Ladder Game")
    print("🔗 Target URL: https://github.com/ShivamJhuria/python-/blob/main/snakandladders.py")
    print("-" * 70)

    # Check dependencies
    print("📦 Checking dependencies...")
    print(f"✅ qrcode: Available")
    print(f"{'✅' if PIL_AVAILABLE else '❌'} PIL/Pillow: {'Available' if PIL_AVAILABLE else 'Not available'}")
    print(f"{'✅' if STYLED_QR_AVAILABLE else '❌'} Styled QR: {'Available' if STYLED_QR_AVAILABLE else 'Not available'}")
    print()

    try:
        # Always create a simple QR code first (most reliable)
        print("🔄 Creating simple QR code...")
        create_simple_qr()

        # Try to create other variations
        print("🔄 Creating basic QR code...")
        generate_basic_qr()

        print("🔄 Creating styled QR code...")
        generate_styled_qr()

        print("🔄 Creating game-themed QR code...")
        generate_game_themed_qr()

        print("🔄 Creating high contrast QR code...")
        generate_high_contrast_qr()

        # Test the QR codes
        test_qr_code()

        print("\n" + "=" * 70)
        print("🎉 SUCCESS! Your QR codes are ready!")
        print("📂 Generated files:")
        print("   • simple_snake_ladder_qr.png (most reliable)")
        print("   • snake_ladder_basic_qr.png")
        print("   • snake_ladder_styled_qr.png")
        print("   • snake_ladder_themed_qr.png")
        print("   • snake_ladder_high_contrast_qr.png")
        print()
        print("📱 Scan any QR code to access your Snake and Ladder game!")
        print("🎯 Recommended: Use 'simple_snake_ladder_qr.png' for guaranteed compatibility")
        print("=" * 70)

    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("\n🔧 To install required packages:")
        print("   pip install qrcode[pil]")
        print("   pip install pillow")
        print("\n💡 For basic QR codes only:")
        print("   pip install qrcode")

    except Exception as e:
        print(f"❌ An error occurred: {e}")
        print("\n🔧 Try installing dependencies:")
        print("   pip install qrcode[pil] pillow")