/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["../templates/**/*.{html,js}"],
    theme: {
        extend: {
            fontFamily: {
                'body': ['montserrat', 'roboto', 'sans-serif'],
            },
        }
    },
    plugins: [
        require('@tailwindcss/typography'),
        // ...
    ],
}