import numpy_financial as npf
import matplotlib.pyplot as plt

def calculate_npv(rate, cash_flows):
    """
    Calculate the Net Present Value (NPV) based on a given discount rate and list of cash flows.
    
    Parameters:
        rate (float): Discount rate as a decimal.
        cash_flows (list): List of cash flows where the first cash flow is at time 0.
    
    Returns:
        float: The calculated NPV.
    """
    try:
        return npf.npv(rate, cash_flows)
    except Exception as e:
        print(f"Error calculating NPV: {e}")
        return None

def calculate_irr(cash_flows):
    """
    Calculate the Internal Rate of Return (IRR) based on a list of cash flows.
    
    Parameters:
        cash_flows (list): List of cash flows where the first cash flow is at time 0.
        
    Returns:
        float: The calculated IRR as a decimal.
    """
    try:
        return npf.irr(cash_flows)
    except Exception as e:
        print(f"Error calculating IRR: {e}")
        return None

if __name__ == '__main__':
    # Define initial cash flows
    cash_flows = [-250000000, 45000000, 45000000, 45000000, 45000000, 45000000, 45000000, 45000000, 45000000]
    
    # Define a range of discount rates from 0% to 20%
    discount_rates = [0.01 * i for i in range(0, 21)]
    
    # Calculate NPVs for different discount rates
    npv_values = [calculate_npv(rate, cash_flows) for rate in discount_rates if calculate_npv(rate, cash_flows) is not None]
    
    # Calculate IRR
    irr = calculate_irr(cash_flows)
    if irr is not None:
        print(f"Internal Rate of Return (IRR): {irr:.4%}")

    # Print NPV values for different discount rates
    print("Net Present Value (NPV) for different discount rates:")
    for i, rate in enumerate(discount_rates):
        print(f"Discount Rate: {rate:.2%}, NPV: {npv_values[i]:.4f}")

    # Generate NPV Profile plot
    plt.plot(discount_rates, npv_values)
    plt.xlabel("Discount Rate")
    plt.ylabel("Net Present Value (NPV)")
    plt.title("NPV Profile")

    # Plot IRR on the NPV Profile
    if irr is not None:
        plt.plot(irr, calculate_npv(irr, cash_flows), 'ro')
        plt.annotate(f'IRR: {irr:.4%}', xy=(irr, calculate_npv(irr, cash_flows)), xytext=(irr, calculate_npv(irr, cash_flows) + 500),
                     arrowprops=dict(arrowstyle='->', color='blue'))
    
    plt.grid(True)
    plt.show()
