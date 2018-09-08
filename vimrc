" Mustafa's .vimrc

" vim-plug config
set runtimepath+='~/.vim'
call plug#begin('~/.vim/plugged')

Plug 'https://github.com/w0ng/vim-hybrid'

Plug 'https://github.com/kien/ctrlp.vim.git'

Plug 'elixir-lang/vim-elixir'

Plug 'https://github.com/slashmili/alchemist.vim'

Plug 'https://github.com/othree/yajs.vim'

Plug 'itchyny/lightline.vim'

call plug#end()

" key maps
" map <C-n> :NERDTreeToggle<CR>

" for powerline
:set laststatus=2

filetype plugin indent on
set expandtab ts=2 sw=2 ai

" set VI no compatible to avoide side effects 
set nocompatible

" leader
let mapleader="\<Space>"
" synthax on
syntax enable

" show line numbers
set number
set relativenumber

" normal backspace.. jus copied it from example 
set backspace=2

set mouse=a

set listchars=eol:¬,nbsp:_,tab:→\ ,trail:~,extends:>,precedes:<,space:·

set list
  
" theme stuff
set background=dark
colorscheme hybrid 

" for ignoring files/folders
set wildignore+=*/tmp/*,*/node_modules/*,*.so,*.swp,*.zip
