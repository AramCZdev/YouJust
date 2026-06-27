#!/bin/bash

_youjust_completion() {
    local cur="${COMP_WORDS[1]}"

    COMPREPLY=($(compgen -W "
        install remove update upgrade
        createfile createfolder delete
        showfile list
        copy move rename
        showsystem
        see ip
        see processes
        see space
        see whereami
        help gethelp
        clear reboot shutdown
    " -- "$cur"))
}

complete -F _youjust_completion youjust