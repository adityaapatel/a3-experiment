library(ggplot2)

# load data
df <- read.csv("trials/master.csv")

# filter by visualization type
df$type <- factor(
  sub("_[0-9]+$", "", df$Vis),
  levels = c("bar", "stacked", "donut")
)

# plot with mean and 95% bootstrapped CI
r_plot <- ggplot(df, aes(x = Error, y = type)) +
  
  # mean 
  stat_summary(
    fun = mean,
    geom = "point",
    size = 3,
    color = "black"
  ) +
  
  # 95% bootstrapped CI
  stat_summary(
    fun.data = mean_cl_boot,
    geom = "errorbarh",
    height = 0.2,
    color = "black"
  ) +

  # labels
  labs(
    x = "Log Error",
    y = "Vis Type",
    title = "Mean Absolute Error by Vis Type with 95% Bootstrapped CI"
  ) +
  
  theme_minimal(base_size = 12)

r_plot
