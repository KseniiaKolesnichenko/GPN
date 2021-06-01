import React from 'react'

import { Header } from './header'
import { Footer } from './footer'
import { Main } from './main'

// Possible routes
export const Layout = () => (
    <React.Fragment>
        <Header />
        <Main />
        <Footer />
    </React.Fragment>
)
