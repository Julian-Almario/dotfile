#!/bin/bash
#Script para enlazar dotfiles

DOTFILES_DIR=$(pwd)

echo "Creado enlaces..."

ln -sf "$DOTFILES_DIR/.bashrc" "$HOME/.bashrc"

mkdir -p "$HOME/.config"
ln -sf "$DOTFILES_DIR/.config" "$HOME/.config"

mkdir -p "$HOME/Imágenes/Wallpapers"
ln -sf "$DOTFILES_DIR/Wallpapers" "$HOME/Imágenes/Wallpapers"

echo "Enlaces creado :)"

