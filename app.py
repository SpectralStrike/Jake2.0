# import openai
# import streamlit as st 


# openai.api_key = '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'

# def generate_text(prompt, max_tokens=500):
#     response = openai.Completion.create(
#         engine="text-davinci-003",  # Use the GPT-3.5 Turbo engine
#         prompt=prompt,
#         max_tokens=max_tokens
#     )
#     return response.choices[0].text.strip()


# small_business_options = [
#     "Animal care",
#     "Auto service & repair",
#     "Beauty & barber",
#     "Contractor & trades",
#     "Distributor",
#     "Food & beverage",
#     "Healthcare",
#     "Professional services",
#     "Real estate & construction",
#     "Religious organization",
#     "Retail shop or service"
# ]

# user_choice = None
# employee_choice = None
# asset_choices = None

# # Check if user_choice, employee_choice, and asset_choices are already set
# if user_choice is None:
#     print("Please choose one of the small businesses:\n")
#     for index, option in enumerate(small_business_options, start=1):
#         print(f"{index}. {option}")
    
#     user_choice = input("Enter the number corresponding to your choice: ")

#     # Validate the user's input to ensure it's a number and within the valid range.
#     try:
#         user_choice = int(user_choice)
#         if 1 <= user_choice <= len(small_business_options):
#             chosen_business = small_business_options[user_choice - 1]
#             print(f"You have chosen: {chosen_business}")
#         else:
#             print("Invalid choice. Please enter a number within the valid range.")
#     except ValueError:
#         print("Invalid input. Please enter a number.")

# # Check if employee_choice is already set
# if employee_choice is None:
#     # Now, ask the user about the number of employees.
#     print("\nHow many employees do you have?")
#     print("1. No employees")
#     print("2. 1-4 employees")
#     print("3. 5-100 employees")
#     print("4. 101+ employees")
#     employee_choice = input("Enter the number corresponding to your choice: ")

#     # Validate the user's input for the number of employees.
#     try:
#         employee_choice = int(employee_choice)
#         if employee_choice == 1:
#             print("You have selected 'No employees'.")
#         elif employee_choice == 2:
#             print("You have selected '1-4 employees'.")
#         elif employee_choice == 3:
#             print("You have selected '5-100 employees'.")
#         elif employee_choice == 4:
#             print("You have selected '101+ employees'.")
#         else:
#             print("Invalid choice. Please enter a valid number.")
#     except ValueError:
#         print("Invalid input. Please enter a number.")

# # Check if asset_choices is already set
# if asset_choices is None:
#     # Now, ask about the assets.
#     print("\nWhich assets do you have? Select all that apply:")
#     print("1. Building I own for my primary business location or lease to others")
#     print("2. Business property (e.g., furniture, equipment) and inventory at my primary location")
#     print("3. Business inventory and equipment is away from my primary location")
#     print("4. Vehicles used for my business")
#     asset_choices = input("Enter the numbers corresponding to your choices, separated by spaces: ")

#     # Split the user's input into individual choices.
#     asset_choices = asset_choices.split()

#     # Process and display the selected asset choices.
#     for choice in asset_choices:
#         if choice == "1":
#             print("You have selected 'Building I own for my primary business location or lease to others'.")
#         elif choice == "2":
#             print("You have selected 'Business property and inventory at your primary location'.")
#         elif choice == "3":
#             print("You have selected 'Business inventory and equipment is away from primary location'.")
#         elif choice == "4":
#             print("You have selected 'Vehicles used for your business'.")
#         else:
#             print(f"Invalid choice: {choice}. Please enter valid numbers.")
            


# prompt = f"""
# System: You are a helpful insurance chatbot that advises small business owners on insurance policies. Recommend an insurance policy based on the user's situation and the provided context.
# Context: Possible insurance policies are Business Owners Policy (BOP), Commercial liability umbrella policy (CLUP), and Workers’ compensation. 
# For small business owners, property and liability coverages are included in one combined package, known as a BOP. We’ve suggested a BOP based on the industry you selected. 
# This insurance package helps protect you against the unexpected risks of doing business. 
# A CLUP provides you with extra liability coverage for the worst-case scenarios that can result in costly lawsuits for your business. 
# You may also need a CLUP to fulfill contractual requirements with landlords or clients. You can increase your liability protection over multiple policies at once. 
# Nearly every state requires businesses to carry workers’ comp insurance so it’s important to consider this coverage. In case of an accident, coverage to help take care of your employees and protect your business from major financial loss can be beneficial.
# User: What insurance policies should I get given I'm in the {user_choice} business and I have {employee_choice} working for my company and I'm have these criteria that apply to me {asset_choices}
# Assistant: """
# response = generate_text(prompt)
# print(response) 

import openai
import streamlit as st

openai.api_key = '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'

def generate_text(prompt, max_tokens=500):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens
    )
    st.write("Assistant:")
    st.write(response.choices[0].text.strip())

small_business_options = [
    "Animal care",
    "Auto service & repair",
    "Beauty & barber",
    "Contractor & trades",
    "Distributor",
    "Food & beverage",
    "Healthcare",
    "Professional services",
    "Real estate & construction",
    "Religious organization",
    "Retail shop or service"
]

user_choice = None
employee_choice = None
asset_choices = None

# Streamlit app header
st.title("Small Business Insurance Advisor")

# Check if user_choice, employee_choice, and asset_choices are already set
if user_choice is None:
    st.write("Please choose one of the small businesses:")
    user_choice = st.selectbox("Select a business type:", small_business_options)

# Check if employee_choice is already set
if employee_choice is None:
    st.write("How many employees do you have?")
    employee_choice = st.radio("Select the number of employees:", [" No employees", " 1-4 employees", " 5-100 employees", " 101+ employees" ], index=0)

# Check if asset_choices is already set
if asset_choices is None:
    st.write("Which assets do you have? Select all that apply:")
    asset_choices = st.multiselect(
        "Select asset options:",
        ["Building I own for my primary business location or lease to others",
         "Business property and inventory at my primary location",
         "Business inventory and equipment is away from the primary location",
         "Vehicles used for my business"]
    )


# Display user choices
st.write(f"You have chosen the business type: {user_choice}")
st.write(f"You have selected '{employee_choice}' employees.")
st.write("You have selected the following asset criteria:")
for choice in asset_choices:
    st.write(f"- {choice}")



prompt = f"""
System: You are a helpful insurance chatbot that advises small business owners on insurance policies. Recommend an insurance policy based on the user's situation and the provided context.
Context: Possible insurance policies are Business Owners Policy (BOP), Commercial liability umbrella policy (CLUP), and Workers’ compensation. 
For small business owners, property and liability coverages are included in one combined package, known as a BOP. We’ve suggested a BOP based on the industry you selected. 
This insurance package helps protect you against the unexpected risks of doing business. 
A CLUP provides you with extra liability coverage for the worst-case scenarios that can result in costly lawsuits for your business. 
You may also need a CLUP to fulfill contractual requirements with landlords or clients. You can increase your liability protection over multiple policies at once. 
Nearly every state requires businesses to carry workers’ comp insurance so it’s important to consider this coverage. In case of an accident, coverage to help take care of your employees and protect your business from major financial loss can be beneficial.
User: What insurance policies should I get given I'm in the {user_choice} business and I have {employee_choice} working for my company and I have these criteria that apply to me {asset_choices}
Assistant: """

if st.button("Submit"):
    on_click=generate_text(prompt)
# response = generate_text(prompt)

# st.write("Assistant:")
# st.write(response)


