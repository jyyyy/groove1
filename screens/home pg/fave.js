import * as React from 'react';
import { Button, View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { useEffect } from 'react';
import * as Font from 'expo-font';


const Fave = ({ navigation }) => {
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
                <Text style={styles.txt1}>Favourite/Frequently visited websites</Text>
                
            </View>

            <View style={styles.box}>
                <Text style={styles.txt2}>No websites have been added yet!</Text>
            </View>

            <View style={styles.cont2}>

                <TouchableOpacity
                    style={styles.log0but2}
                    underlayColor = "#135C63"
                    onPress={() => navigation.goBack()}
                >
                    <Text style={styles.log0bt2}>Go Back</Text>

                </TouchableOpacity>
            </View>


        </View>
    );
};


const styles = StyleSheet.create({
    bgc: {
        flex: 1,
        backgroundColor: '#FFEEDB',
        alignItems: 'center',
    },

    box:{
        width: 1000,
        height: 300,
        paddingTop: 20,
        borderRadius:20,
        backgroundColor:'#FFD0C6',
        alignItems: 'center',
        display:'flex',

    },

    txt1: {
        fontFamily: 'gochi-hand',
        fontStyle: 'normal',
        fontWeight: '400',
        fontSize: 60,
        lineHeight: 71,
        display: 'flex',
        alignItems: 'center',
        color: '#000',
    },    
    
    txt2: {
        fontFamily: 'gochi-hand',
        fontStyle: 'normal',
        fontWeight: '400',
        fontSize: 40,
        lineHeight: 71,
        display: 'flex',
        alignItems: 'center',
        color: '#4E4E4E',
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

    cont1: {
        paddingTop: 80,
        justifyContent: 'center',
        alignItems: 'center',
        paddingBottom: 40,
    },


    cont2: {
        flex: 1,
        paddingHorizontal: 16,
        paddingTop: 82,
        justifyContent: 'center',
        alignItems: 'center',
    },

});

  


export default Fave;