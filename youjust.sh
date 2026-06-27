youjust() {
    local output

    # call binary safely
    output=$(command youjust "$@")
    output=$(echo "$output" | xargs)

    # execute cd inside current shell
    if [[ "$output" == cd\ * ]]; then
        builtin cd "${output#cd }"
        return
    fi

    echo "$output"
}