import * as React from 'react';
import { Button, View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { useEffect } from 'react';
import * as Font from 'expo-font';


const Login0 = ({ navigation }) => {
    useEffect(() => {
        loadFonts();
    }, []);

    const loadFonts = async () => {
        await Font.loadAsync({
            'gochi-hand': require('../fonts/GochiHand-Regular.ttf'),
        });
    };
    return (
        <View style={styles.bgc} >
            <View style={styles.cont1}>
                <TouchableOpacity
                    style={styles.log0but1}
                    underlayColor = "#135C63"
                    onPress={() => navigation.navigate('NoAcc')}
                >
                    <Text style={styles.log0bt1}>Continue without Account</Text>

                </TouchableOpacity>

                <TouchableOpacity
                    style={styles.log0but2}
                    underlayColor = "#135C63"
                    onPress={() => navigation.navigate('Login1')}
                >
                    <Text style={styles.log0bt2}>Log in</Text>

                </TouchableOpacity>

                <TouchableOpacity
                    style={styles.log0but3}
                    underlayColor = "#135C63"
                    onPress={() => navigation.navigate('CreateAcc')}
                >
                    <Text style={styles.log0bt2}>Create an account</Text>

                </TouchableOpacity>
                
            </View>

            <View style={styles.cont2}>
                <TouchableOpacity
                    style={styles.log0but4}
                    underlayColor = "#B484A7"
                    onPress={() => navigation.navigate('NoAcc')}
                >
                    <Text style={styles.log0bt2}>Need help? Click here to rewatch the tutorial!</Text>
                </TouchableOpacity>
            </View>


        </View>
    );
};


const styles = StyleSheet.create({
    bgc: {
        flex: 1,
        backgroundColor: '#FFEEDB',
    },

    log0but1: {
        width: 742,
        height: 149,
        backgroundColor: '#177E89',
        borderRadius: 20,
        justifyContent: 'center',
        alignItems: 'center',
        shadowColor: '#000',
        shadowOffset: { width: 3, height: 5 },
        shadowOpacity: 0.4,
        shadowRadius: 4,
        elevation: 5,
        marginBottom: 38,

    },    

    log0bt1: {
        fontFamily: 'gochi-hand',
        fontStyle: 'normal',
        fontWeight: '400',
        fontSize: 60,
        lineHeight: 71,
        display: 'flex',
        alignItems: 'center',
        textDecorationLine: 'underline',
        color: '#FFEEDB',
    },


    log0but2: {
        width: 280,
        height: 92,
        backgroundColor: '#177E89',
        borderRadius: 20,
        justifyContent: 'center',
        alignItems: 'center',
        shadowColor: '#000',
        shadowOffset: { width: 3, height: 5 },
        shadowOpacity: 0.4,
        shadowRadius: 4,
        elevation: 5,
        marginBottom: 38,
    },
    
    log0bt2: {
        fontFamily: 'gochi-hand',
        fontStyle: 'normal',
        fontWeight: '400',
        fontSize: 45,
        lineHeight: 53,
        display: 'flex',
        alignItems: 'center',
        textDecorationLine: 'underline',
        color: '#FFEEDB',
    },

    log0but3: {
        width: 438,
        height: 92,
        backgroundColor: '#177E89',
        borderRadius: 20,
        justifyContent: 'center',
        alignItems: 'center',
        shadowColor: '#000',
        shadowOffset: { width: 3, height: 5 },
        shadowOpacity: 0.4,
        shadowRadius: 4,
        elevation: 5,
    },


    log0but4: {
        width: 922,
        height: 83,
        backgroundColor: '#B484A7',
        borderRadius: 20,
        justifyContent: 'center',
        alignItems: 'center',
        shadowColor: '#000',
        shadowOffset: { width: 3, height: 5 },
        shadowOpacity: 0.4,
        shadowRadius: 4,
        elevation: 5,
    },

    cont1: {
        paddingHorizontal: 16,
        paddingTop: 162,
        justifyContent: 'center',
        alignItems: 'center',
    },

    cont2: {
        flex: 1,
        paddingHorizontal: 16,
        paddingTop: 82,
        justifyContent: 'center',
        alignItems: 'center',
    },

});

  


export default Login0;