youjust() {
    local output

    output="$(python3 /home/aramcz/Documents/GitHub/YouJust/youjust.py "$@")"

    if [[ "$output" == cd\ * ]]; then
        builtin cd -- "${output#cd }"
        return
    fi

    printf '%s\n' "$output"
}