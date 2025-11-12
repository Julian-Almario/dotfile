# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
alias inf='neofetch'
alias bye='sudo shutdown now'
alias diskinfo="sudo fdisk -l"
alias wifi="nmtui"
alias gitoff="eval "$(ssh-agent -k)""

# color terminal

wal -n -q -i /home/julian/Imágenes/Wallpapers/77.jpg

# init deamon programs
eval "$(ssh-agent -s)"
eval "$(starship init bash)"

