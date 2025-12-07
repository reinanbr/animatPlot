
# Usage example
if __name__ == "__main__":
    # Generate 128 timestamps every 3 hours starting from now
    timestamps = generate_timestamps()
    
    # Display first 5 and last 5
    print("First 5 timestamps:")
    for ts in timestamps[:5]:
        print(ts.strftime("%Y-%m-%d %H:%M:%S"))
    
    print("\n...")
    
    print("\nLast 5 timestamps:")
    for ts in timestamps[-5:]:
        print(ts.strftime("%Y-%m-%d %H:%M:%S"))
    
    print(f"\nTotal timestamps generated: {len(timestamps)}")
    
    # Example with custom start date
    custom_date = datetime(2025, 1, 1, 0, 0, 0)
    custom_timestamps = generate_timestamps(quantity=10, start_date=custom_date)
    
    print("\n\nExample with custom start date (01/01/2025):")
    for ts in custom_timestamps:
        print(ts.strftime("%Y-%m-%d %H:%M:%S"))