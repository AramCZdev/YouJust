youjust() {
    local output

    output=$(command youjust "$@")

    if [[ "$output" == cd\ * ]]; then
        builtin cd "${output:3}"
        return
    fi

    echo "$output"
}