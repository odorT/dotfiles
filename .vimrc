" My vimrc

set nocompatible
set relativenumber
set nu rnu
set noswapfile
set nobackup
set hlsearch
set ignorecase
set incsearch
set tabstop=4
set smartindent
set shiftwidth=4
set smarttab
set path+=**
set wildmenu
set hidden
set t_Co=256
set clipboard=unnamedplus
set laststatus=2
set noshowmode

filetype off
filetype plugin indent on

syntax enable

" Vundle configuration
set rtp+=~/.vim/bundle/Vundle.vim

" Plugins
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'tpope/vim-fugitive'
Plugin 'preservim/nerdtree'
Plugin 'jiangmiao/auto-pairs'
Plugin 'dense-analysis/ale'
Plugin 'itchyny/lightline.vim'
Plugin 'suan/vim-instant-markdown', {'rtp': 'after'}
Plugin 'PotatoesMaster/i3-vim-syntax'
Plugin 'kovetskiy/sxhkd-vim'
Plugin 'vim-python/python-syntax'
Plugin 'ap/vim-css-color'
Plugin 'sonph/onehalf', { 'rtp': 'vim' }
Plugin 'morhetz/gruvbox'

call vundle#end() 


let g:rehash256 = 1
let g:listline = {
	\ 'colorscheme': 'wombat',
	\ }

colorscheme onehalfdark
let g:airline_theme='onehalfdark'
