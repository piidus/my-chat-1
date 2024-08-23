# import psutil
# import time

# def memory_profiler(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         memory_info = psutil.Process().memory_info()
#         memory_usage_in_mb = memory_info.rss / 1024 / 1024

#         result = func(*args, **kwargs)

#         end_time = time.time()
#         elapsed_time = end_time - start_time
#         memory_info = psutil.Process().memory_info()
#         final_memory_usage_in_mb = memory_info.rss / 1024 / 1024

#         print(f"Function: {func.__name__}")
#         print(f"Memory usage before: {memory_usage_in_mb:.2f} MB")
#         print(f"Memory usage after: {final_memory_usage_in_mb:.2f} MB")
#         print(f"Elapsed time: {elapsed_time:.2f} seconds")
#         print()

#         return result

#     return wrapper

# @memory_profiler
# def my_flet_function():
#     # Your Flet app code here
#     pass

# if __name__ == "__main__":
#     my_flet_function()