"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const core_1 = require("@oclif/core");
const hook = async function (options) {
    const npmPackageNames = ['@heroku/plugin-ai', '@heroku-cli/plugin-ai'];
    if (options.plugin.type !== 'npm' || !npmPackageNames.includes(options.plugin.name))
        return;
    core_1.ux.warn('\n\nThis pilot feature is a Beta Service. You may opt to try such Beta Service in your sole discretion. ' +
        'Any use of the Beta Service is subject to the applicable Beta Services Terms provided at ' +
        'https://www.salesforce.com/company/legal/customer-agreements/. While use of the pilot feature itself is free, ' +
        'to the extent such use consumes a generally available Service, you may be charged for that consumption as set ' +
        'forth in the Documentation. Your continued use of this pilot feature constitutes your acceptance of the foregoing.\n\n' +
        'For clarity and without limitation, the various third-party machine learning and generative artificial intelligence ' +
        '(AI) models and applications (each a “Platform”) integrated with the Beta Service are Non-SFDC Applications, ' +
        'as that term is defined in the Beta Services Terms. Note that these third-party Platforms include features that use ' +
        'generative AI technology. Due to the nature of generative AI, the output that a Platform generates may be ' +
        'unpredictable, and may include inaccurate or harmful responses. Before using any generative AI output, Customer is ' +
        'solely responsible for reviewing the output for accuracy, safety, and compliance with applicable laws and third-party ' +
        'acceptable use policies. In addition, Customer’s use of each Platform may be subject to the Platform’s own terms and ' +
        'conditions, compliance with which Customer is solely responsible.\n');
    const response = await core_1.ux.prompt('Continue? (Y/N)');
    if (response.toUpperCase() !== 'Y') {
        core_1.ux.error('Canceled', { exit: 1 });
    }
};
exports.default = hook;
