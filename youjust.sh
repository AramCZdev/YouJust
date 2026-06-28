youjust() {
    local output

    output=$(command youjust "$@")

    # trim whitespace safely
    output=$(echo "$output" | sed 's/^[ \t]*//;s/[ \t]*$//')

    # execute cd in current shell if returned
    if [[ "$output" == cd\ * ]]; then
        builtin cd "${output#cd }"
        return
    fi

    echo "$output"
}