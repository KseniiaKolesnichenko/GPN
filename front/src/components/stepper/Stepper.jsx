import React from 'react'

import LibStepper from 'react-stepper-horizontal'

const STEPS = [
    {
        title: 'Search'
    },
    {
        title: 'Settings'
    },
    {
        title: 'Enjoy'
    }
]

export const Stepper = () => (
    <LibStepper steps={STEPS} activeStep={0} />
)