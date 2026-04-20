mean_accuracy <- function(df) {
  if (nrow(df) == 0) {
    stop("df cannot be empty")
  }
  mean(df$accuracy)
}
