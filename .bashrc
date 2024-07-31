#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='exa -al --color=always --group-directories-first'
alias la='exa -a --color=always --group-directories-first'
alias ..="cd .."
alias ...="cd ../.."
alias .3="cd ../../.."
alias .4="cd ../../../.."
alias .5="cd ../../../../.."
alias vim="nvim"
alias pacsyu="sudo pacman -Syu"
alias yaysua="yay -Sua 1--noconfirm"
alias yaysyu="yay -Syu --noconfirm"
alias grep='grep --color=auto'

alias openconfig="code ~/.config/qtile/config.py"
alias openbashrc="code ~/.bashrc"
alias openpicom="code ~/.config/picom/picom.conf"

PS1='[\u@\h \W]\$ '
