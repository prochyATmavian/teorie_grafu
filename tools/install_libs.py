#!/usr/bin/env python3
"""
Skript pro instalaci knihoven do venv.
"""

import subprocess
import sys
import os

def main():
    # Zjistíme, zda jsme ve venv
    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )
    
    print(f"Python: {sys.executable}")
    print(f"Ve venv: {'ANO' if in_venv else 'NE'}")
    print()
    
    if not in_venv:
        print("⚠️  Nejste ve virtuálním prostředí!")
        print("Spusťte:")
        print("  source venv/bin/activate")
        print("  python3 install_libs.py")
        sys.exit(1)
    
    # Knihovny k instalaci
    packages = ['matplotlib', 'networkx', 'graphviz']
    
    print("📦 Instaluji knihovny...")
    print()
    
    for package in packages:
        print(f"Instaluji {package}...")
        try:
            subprocess.check_call(
                [sys.executable, '-m', 'pip', 'install', package],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            print(f"  ✓ {package} nainstalován")
        except subprocess.CalledProcessError as e:
            print(f"  ✗ Chyba při instalaci {package}: {e}")
    
    print()
    print("✅ Hotovo!")
    print()
    
    # Ověření instalace
    print("🔍 Ověřuji instalaci...")
    for package in packages:
        try:
            __import__(package)
            print(f"  ✓ {package} - OK")
        except ImportError:
            print(f"  ✗ {package} - CHYBA")
    
    print()
    print("Pro spuštění programu použijte:")
    print("  python3 run.py <soubor.tg>")

if __name__ == "__main__":
    main()

