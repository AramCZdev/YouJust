#!/bin/bash

# only load in interactive shells
if [[ $- != *i* ]]; then
    return
fi

_youjust_completion() {
    local cur="${COMP_WORDS[COMP_CWORD]}"

    COMPREPLY=($(compgen -W "
        install remove update upgrade
        create file create folder delete
        show file list
        copy move rename
        showsystem
        see ip
        see processes
        see space
        see whereami
        go into
        ping kill
        help gethelp
        clear reboot shutdown
    " -- "$cur"))
}

youjust() {
    local output
    output=$(youjust "$@")   # IMPORTANT: use installed binary
    output=$(echo "$output" | xargs)

    if [[ "$output" == cd\ * ]]; then
        builtin cd "${output:3}"
        return
    fi

    echo "$output"
}

complete -F _youjust_completion youjust