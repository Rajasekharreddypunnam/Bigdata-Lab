def count_consecutive_characters(input_string):
    result = []
    count = 1

    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i-1]:
            count += 1
        else:
            if count > 1:
                result.append(input_string[i-1] + str(count))
            else:
                result.append(input_string[i-1])
            count = 1

    if count > 1:
        result.append(input_string[-1] + str(count))
    else:
        result.append(input_string[-1])

    return ''.join(result)

# Example Usage
# input_str = "abcaaabbb"
input_str = "abcd"

output_str = count_consecutive_characters(input_str)
print(output_str)
