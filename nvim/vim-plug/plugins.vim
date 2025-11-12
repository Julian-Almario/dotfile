call plug#begin('~/.config/nvim/autoload/plugged')

	Plug 'sheerun/vim-polyglot'
	Plug 'preservim/nerdtree'
	Plug 'windwp/nvim-autopairs'
	Plug 'morhetz/gruvbox'
	Plug 'vim-airline/vim-airline'

call plug#end()

colorscheme gruvbox
:highlight Normal ctermbg=NONE guibg=NONE
:set number relativenumber
