# GAR Vulnerability Curve Parameters

This repository contains a Python script designed to process Global Assessment Report (GAR) vulnerability curve data. The script fits a curve to these data points and derives the parameters mu (μ) and sigma (σ), essential for risk and vulnerability assessment in disaster risk reduction and management.

## Features

- **Curve Fitting:** Utilizes log-normal cumulative distribution functions (CDF) to fit curves to vulnerability data.
- **Parameter Derivation:** Calculates μ and σ values for each curve, integral for statistical analysis.
- **Versatility:** Supports different types of hazards including Ash, Earthquake, Flood, Tsunami, and Wind.
- **Data Export:** Produces a CSV file with the GAR building identifier, along with calculated μ and σ.
- **Visualization:** Generates figures for each curve for result validation and sanity checks.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3
- Libraries: `numpy`, `pandas`, `scipy`, `matplotlib`

### Installation

Clone the repository to your local machine:


### Usage

1. Place your GAR vulnerability data in the appropriate directory. The directory structure should follow the format `GAR15_Regional_Vulnerability_Functions/[hazard]/`, where `[hazard]` can be Ash, Earthquake, Flood, Tsunami, or Wind.
2. Adjust the `hazard` variable in the script to select the specific type of hazard data you want to process. You can set it to a list of hazards to process multiple types.
3. Run the script


### Output

- A CSV file named `[hazard]_CDV_parameters.csv`, containing the building code, μ, and σ values for each curve.
- A series of figures saved in the `Figures` folder for visual verification of the curve fitting.

## Contributing

Contributions to enhance this script or extend its capabilities are welcome. Please feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Thanks to the contributors and maintainers of the GAR vulnerability data.
- Appreciation to the open-source community for continuous support and inspiration.

## Disclaimer

This script is provided as is, and it is up to the user to verify the correctness and applicability of the results in their context. I highly recommend sanity checking the outputs as I've made some wide ranging assumptions in the script.

## Contact

For any queries or assistance, feel free to contact Josh Hayes.



