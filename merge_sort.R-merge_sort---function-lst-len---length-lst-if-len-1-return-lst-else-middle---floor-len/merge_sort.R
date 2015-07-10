
merge_sort <- function(lst) {
    len <- length(lst)
    if (len <= 1) {
        return (lst)
    } else {
        middle <- floor(len/2)
        list_a <- merge_sort(lst[1:middle])
        list_b <- merge_sort(lst[(middle + 1):len])
        output_list <- merge(list_a, list_b)
        return (output_list)
    }
}

merge <- function(list_a, list_b) {
    output_list <- c()
    while (length(list_a) > 0 && length(list_b) > 0) {
        if (list_a[1] < list_b[1]) {
            output_list <- c(output_list, list_a[1])
            list_a <- list_a[-1]
        } else {
            output_list <- c(output_list, list_b[1])
            list_b <- list_b[-1]
        }
    }
    if (length(list_a) > 0) {
        output_list <- c(output_list, list_a)
    }
    if (length(list_b) > 0) {
        output_list <- c(output_list, list_b)
    }
    return (output_list)
}
