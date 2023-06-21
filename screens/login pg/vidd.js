import * as React from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Image } from 'react-native';
import { useEffect } from 'react';
import * as Font from 'expo-font';


const Vidd = ({ navigation }) => {
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
            <TouchableOpacity 
                style={styles.fullpg}
                onPress={() => navigation.navigate('Login0')}
            >
                <Text style={styles.txt1}>Tutorial Video</Text>
            </TouchableOpacity>

        </View>
    );
};


const styles = StyleSheet.create({
    bgc: {
        flex:1,
        backgroundColor:"#000",
    },

    txt1: {
        fontFamily: 'gochi-hand',
        fontStyle: 'normal',
        fontWeight: '400',
        fontSize: 60,
        lineHeight: 71,
        display: 'flex',
        alignItems: 'center',
        color: '#FFF',
    },
    
    fullpg: {
        alignItems: 'center',
        justifyContent: 'center',
        flex: 1,
    },

});

  


export default Vidd;