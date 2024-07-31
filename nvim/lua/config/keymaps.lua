vim.keymap.set('n', '<leader>h', '<Cmd>noh<CR>', {})
vim.keymap.set('n', '<leader>l', '<Cmd>Lazy<CR>', {})
vim.keymap.set('n', '<leader>ff', require('telescope.builtin').find_files, {})
vim.keymap.set('n', '<leader>fg', require('telescope.builtin').live_grep, {})
